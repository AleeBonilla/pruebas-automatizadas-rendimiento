package taller.rendimiento;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.StringJoiner;
import java.util.TreeMap;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.atomic.AtomicLong;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Registra cada fase: el intervalo UTC desde que sale la primera solicitud hasta
 * que llega la última respuesta, cuántas solicitudes salieron y terminaron, y
 * cuándo salió la última. Con eso se alinean los paneles de Grafana con las
 * fases (Taller.md §6.5) y se comprueba que el generador sostuvo la tasa (§6.4).
 *
 * <p>También guarda una serie de tiempos por bloques de BLOQUE_S segundos, según
 * el momento en que salió cada solicitud. Con ella se ve cómo evoluciona la
 * degradación dentro de una fase y se mide la recuperación después de un pico.
 */
public final class Fases {

  /** Una solicitud: cuándo salió, cuánto tardó y si falló. */
  private record Muestra(long inicio, long duracion, boolean fallida) {}

  /** Una fase. Los hilos de Gatling la actualizan en paralelo. */
  public static final class Fase {
    private final double tasaPrevista;
    private final int duracionPrevistaS;
    private final AtomicLong inicio = new AtomicLong(Long.MAX_VALUE);
    private final AtomicLong ultimoInicio = new AtomicLong(Long.MIN_VALUE);
    private final AtomicLong fin = new AtomicLong(Long.MIN_VALUE);
    private final AtomicLong iniciadas = new AtomicLong();
    private final AtomicLong terminadas = new AtomicLong();
    private final ConcurrentLinkedQueue<Muestra> muestras = new ConcurrentLinkedQueue<>();

    private Fase(double tasaPrevista, int duracionPrevistaS) {
      this.tasaPrevista = tasaPrevista;
      this.duracionPrevistaS = duracionPrevistaS;
    }

    /** Devuelve el instante de salida, que el escenario guarda en la sesión. */
    long marcarInicio() {
      long ahora = System.currentTimeMillis();
      inicio.accumulateAndGet(ahora, Math::min);
      ultimoInicio.accumulateAndGet(ahora, Math::max);
      iniciadas.incrementAndGet();
      return ahora;
    }

    /** Se llama también cuando la solicitud falla: Gatling sigue con el escenario. */
    void marcarFin(long inicioSolicitud, boolean fallida) {
      long ahora = System.currentTimeMillis();
      fin.accumulateAndGet(ahora, Math::max);
      terminadas.incrementAndGet();
      muestras.add(new Muestra(inicioSolicitud, ahora - inicioSolicitud, fallida));
    }

    private String json() {
      long i = inicio.get();
      long u = ultimoInicio.get();
      long f = fin.get();
      if (i == Long.MAX_VALUE || f == Long.MIN_VALUE) {
        return "null";
      }
      return String.format(Locale.ROOT,
          "{\"inicio\": \"%s\", \"fin\": \"%s\", \"inicio_ms\": %d, \"fin_ms\": %d, \"duracion_s\": %.3f,"
              + " \"ultimo_inicio_ms\": %d, \"inyeccion_s\": %.3f, \"iniciadas\": %d, \"terminadas\": %d,"
              + " \"tasa_prevista\": %s, \"duracion_prevista_s\": %d, \"bloques\": %s}",
          Instant.ofEpochMilli(i), Instant.ofEpochMilli(f), i, f, (f - i) / 1000.0,
          u, (u - i) / 1000.0, iniciadas.get(), terminadas.get(),
          tasaPrevista, duracionPrevistaS, bloques(i));
    }

    /** Serie por bloques, contados desde la primera salida de la fase. */
    private String bloques(long desde) {
      long bloqueMs = Parametros.BLOQUE_S * 1000L;
      TreeMap<Long, List<Muestra>> porBloque = new TreeMap<>();
      for (Muestra m : muestras) {
        porBloque.computeIfAbsent((m.inicio() - desde) / bloqueMs, k -> new ArrayList<>()).add(m);
      }
      StringJoiner json = new StringJoiner(", ", "[", "]");
      for (Map.Entry<Long, List<Muestra>> bloque : porBloque.entrySet()) {
        List<Muestra> lista = bloque.getValue();
        long[] duraciones = lista.stream().mapToLong(Muestra::duracion).sorted().toArray();
        long fallidas = lista.stream().filter(Muestra::fallida).count();
        json.add(String.format(Locale.ROOT,
            "{\"desde_s\": %d, \"solicitudes\": %d, \"fallidas\": %d, \"p50_ms\": %d, \"p95_ms\": %d, \"max_ms\": %d}",
            bloque.getKey() * Parametros.BLOQUE_S, duraciones.length, fallidas,
            percentil(duraciones, 50), percentil(duraciones, 95), duraciones[duraciones.length - 1]));
      }
      return json.toString();
    }

    /** Percentil por rango más cercano sobre valores ordenados. */
    private static long percentil(long[] ordenados, double p) {
      int rango = (int) Math.ceil(p / 100 * ordenados.length);
      return ordenados[Math.max(0, rango - 1)];
    }
  }

  private static final Pattern VARIANTE = Pattern.compile("\"variante\"\\s*:\\s*\"([^\"]*)\"");

  private final Map<String, Fase> fases = new LinkedHashMap<>();
  private long inicioSimulacion;
  private String varianteApi = "desconocida";

  /** Crea la fase con la tasa y la duración de su inyección, de las que salen las solicitudes previstas. */
  public synchronized Fase fase(String nombre, double tasa, int duracionS) {
    return fases.computeIfAbsent(nombre, n -> new Fase(tasa, duracionS));
  }

  /**
   * Marca el inicio y pregunta a /salud qué variante atiende de verdad, para
   * que una API levantada con otra variante invalide la ejecución (§6.4).
   */
  public void iniciarSimulacion() {
    inicioSimulacion = System.currentTimeMillis();
    varianteApi = consultarVariante();
  }

  private static String consultarVariante() {
    try (HttpClient cliente = HttpClient.newBuilder().connectTimeout(Duration.ofSeconds(5)).build()) {
      HttpRequest solicitud = HttpRequest.newBuilder(URI.create(Parametros.BASE_URL + "/salud"))
          .timeout(Duration.ofSeconds(5)).GET().build();
      HttpResponse<String> respuesta = cliente.send(solicitud, HttpResponse.BodyHandlers.ofString());
      Matcher coincidencia = VARIANTE.matcher(respuesta.body());
      return respuesta.statusCode() == 200 && coincidencia.find() ? coincidencia.group(1) : "desconocida";
    } catch (IOException e) {
      return "desconocida";
    } catch (InterruptedException e) {
      Thread.currentThread().interrupt();
      return "desconocida";
    }
  }

  /** Escribe fases.json con las fases y los parámetros efectivos de la ejecución. */
  public void escribir(String simulacion) {
    long finSimulacion = System.currentTimeMillis();
    StringBuilder json = new StringBuilder("{\n");
    json.append("  \"simulacion\": \"").append(simulacion).append("\",\n");
    json.append("  \"inicio\": \"").append(Instant.ofEpochMilli(inicioSimulacion)).append("\",\n");
    json.append("  \"fin\": \"").append(Instant.ofEpochMilli(finSimulacion)).append("\",\n");
    json.append("  \"variante_api\": \"").append(varianteApi).append("\",\n");
    json.append(String.format(Locale.ROOT,
        "  \"parametros\": {\"baseUrl\": \"%s\", \"ruta\": \"%s\", \"csv\": \"%s\", \"tasa\": %s,"
            + " \"umbralMs\": %d, \"erroresMaxPct\": %s, \"calentamientoS\": %d, \"medicionS\": %d,"
            + " \"picoTasa\": %s, \"picoS\": %d, \"bloqueS\": %d},%n",
        Parametros.BASE_URL, Parametros.RUTA, Parametros.CSV, Parametros.TASA,
        Parametros.UMBRAL_MS, Parametros.ERRORES_MAX_PCT, Parametros.CALENTAMIENTO_S, Parametros.MEDICION_S,
        Parametros.PICO_TASA, Parametros.PICO_S, Parametros.BLOQUE_S));
    json.append("  \"fases\": {");
    String separador = "\n";
    for (Map.Entry<String, Fase> entrada : fases.entrySet()) {
      json.append(separador).append("    \"").append(entrada.getKey()).append("\": ").append(entrada.getValue().json());
      separador = ",\n";
    }
    json.append("\n  }\n}\n");

    try {
      Path carpeta = Path.of(Parametros.SALIDA);
      Files.createDirectories(carpeta);
      Files.writeString(carpeta.resolve("fases.json"), json, StandardCharsets.UTF_8);
    } catch (IOException e) {
      throw new UncheckedIOException("no se pudo escribir fases.json en " + Parametros.SALIDA, e);
    }
  }
}
