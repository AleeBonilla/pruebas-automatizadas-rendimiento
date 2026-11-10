package taller.rendimiento;

/**
 * Parámetros de las simulaciones. Se leen de las propiedades del sistema
 * (-Dtasa=20), que los scripts del taller toman del perfil
 * config/perfiles/&lt;perfil&gt;.env. Ningún valor de medición se fija en el código.
 */
public final class Parametros {

  /** URL base de la API. Dentro de Compose, el servicio se llama api. */
  public static final String BASE_URL = texto("baseUrl", "http://api:8000");

  /** Operación consultada: productos, o salud para comprobar el generador (Taller.md §7.1). */
  public static final String RUTA = texto("ruta", "productos");

  /** Archivo con los identificadores (encabezado id). En Compose se monta desde base-datos/. */
  public static final String CSV = texto("csv", "/datos/productos.csv");

  /** Llegadas por segundo. En el modelo abierto, es también la tasa de solicitudes. */
  public static final double TASA = decimal("tasa", 20);

  public static final int UMBRAL_MS = entero("umbralMs", 300);
  public static final double ERRORES_MAX_PCT = decimal("erroresMaxPct", 1.0);
  public static final int CALENTAMIENTO_S = entero("calentamientoS", 60);
  public static final int MEDICION_S = entero("medicionS", 180);

  /**
   * Picos (Taller.md §6.3): llegadas por segundo y duración del pico. La base y
   * la recuperación usan TASA; 0 significa que no se indicó.
   */
  public static final double PICO_TASA = decimal("picoTasa", 0);
  public static final int PICO_S = entero("picoS", 30);

  /** Duración de los bloques de la serie de tiempos de fases.json (Taller.md §6.4). */
  public static final int BLOQUE_S = entero("bloqueS", 5);

  /** Carpeta donde la simulación escribe fases.json. */
  public static final String SALIDA = texto("salida", "target/ejecucion");

  private Parametros() {}

  public static boolean consultaProductos() {
    return switch (RUTA) {
      case "productos" -> true;
      case "salud" -> false;
      default -> throw new IllegalArgumentException("ruta debe ser productos o salud, no " + RUTA);
    };
  }

  private static String texto(String nombre, String porDefecto) {
    String valor = System.getProperty(nombre);
    return valor == null || valor.isBlank() ? porDefecto : valor.trim();
  }

  private static int entero(String nombre, int porDefecto) {
    return Integer.parseInt(texto(nombre, Integer.toString(porDefecto)));
  }

  private static double decimal(String nombre, double porDefecto) {
    return Double.parseDouble(texto(nombre, Double.toString(porDefecto)));
  }
}
