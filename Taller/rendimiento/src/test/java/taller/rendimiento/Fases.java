package taller.rendimiento;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.Instant;
import java.util.LinkedHashMap;
import java.util.Locale;
import java.util.Map;
import java.util.concurrent.atomic.AtomicLong;

/**
 * Registra el intervalo UTC de cada fase: desde que sale la primera solicitud
 * hasta que llega la última respuesta. Sirve para alinear los paneles de Grafana
 * con las fases de Gatling (Taller.md §6.5) y para calcular la tasa lograda.
 */
public final class Fases {

  /** Intervalo de una fase. Los hilos de Gatling lo actualizan en paralelo. */
  public static final class Fase {
    private final AtomicLong inicio = new AtomicLong(Long.MAX_VALUE);
    private final AtomicLong fin = new AtomicLong(Long.MIN_VALUE);

    void marcarInicio() {
      inicio.accumulateAndGet(System.currentTimeMillis(), Math::min);
    }

    void marcarFin() {
      fin.accumulateAndGet(System.currentTimeMillis(), Math::max);
    }

    private String json() {
      long i = inicio.get();
      long f = fin.get();
      if (i == Long.MAX_VALUE || f == Long.MIN_VALUE) {
        return "null";
      }
      return String.format(Locale.ROOT,
          "{\"inicio\": \"%s\", \"fin\": \"%s\", \"inicio_ms\": %d, \"fin_ms\": %d, \"duracion_s\": %.3f}",
          Instant.ofEpochMilli(i), Instant.ofEpochMilli(f), i, f, (f - i) / 1000.0);
    }
  }

  private final Map<String, Fase> fases = new LinkedHashMap<>();
  private long inicioSimulacion;

  public synchronized Fase fase(String nombre) {
    return fases.computeIfAbsent(nombre, n -> new Fase());
  }

  public void iniciarSimulacion() {
    inicioSimulacion = System.currentTimeMillis();
  }

  /** Escribe fases.json con los intervalos y los parámetros efectivos de la ejecución. */
  public void escribir(String simulacion) {
    long finSimulacion = System.currentTimeMillis();
    StringBuilder json = new StringBuilder("{\n");
    json.append("  \"simulacion\": \"").append(simulacion).append("\",\n");
    json.append("  \"inicio\": \"").append(Instant.ofEpochMilli(inicioSimulacion)).append("\",\n");
    json.append("  \"fin\": \"").append(Instant.ofEpochMilli(finSimulacion)).append("\",\n");
    json.append(String.format(Locale.ROOT,
        "  \"parametros\": {\"baseUrl\": \"%s\", \"ruta\": \"%s\", \"csv\": \"%s\", \"tasa\": %s,"
            + " \"umbralMs\": %d, \"erroresMaxPct\": %s, \"calentamientoS\": %d, \"medicionS\": %d},%n",
        Parametros.BASE_URL, Parametros.RUTA, Parametros.CSV, Parametros.TASA,
        Parametros.UMBRAL_MS, Parametros.ERRORES_MAX_PCT, Parametros.CALENTAMIENTO_S, Parametros.MEDICION_S));
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
