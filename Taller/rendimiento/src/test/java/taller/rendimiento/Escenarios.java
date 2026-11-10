package taller.rendimiento;

import static io.gatling.javaapi.core.CoreDsl.*;
import static io.gatling.javaapi.http.HttpDsl.*;

import io.gatling.javaapi.core.ChainBuilder;
import io.gatling.javaapi.core.ScenarioBuilder;
import io.gatling.javaapi.http.HttpProtocolBuilder;
import io.gatling.javaapi.http.HttpRequestActionBuilder;

/** Piezas comunes a las simulaciones del taller. */
public final class Escenarios {

  /** Atributo de sesión con el instante en que salió la solicitud. */
  private static final String INICIO = "inicioSolicitud";

  private Escenarios() {}

  /**
   * Protocolo HTTP. Gatling no reintenta solicitudes por su cuenta, así que no se
   * registran visitas que el escenario no hizo (Taller.md §4.1).
   */
  public static HttpProtocolBuilder protocolo() {
    return http.baseUrl(Parametros.BASE_URL).acceptHeader("application/json");
  }

  /**
   * Escenario de una fase: cada usuario virtual hace una consulta y termina
   * (modelo abierto, Taller.md §6.1). El nombre de la solicitud es el de la fase,
   * así las aserciones se aplican solo a la medición con details(nombre).
   */
  public static ScenarioBuilder consulta(String nombre, Fases.Fase fase) {
    ChainBuilder solicitud = exec(session -> session.set(INICIO, fase.marcarInicio()))
        .exec(Parametros.consultaProductos() ? producto(nombre) : salud(nombre))
        .exec(session -> {
          // Cada usuario hace una sola solicitud: si la sesión falló, falló esa.
          fase.marcarFin(session.getLong(INICIO), session.isFailed());
          return session;
        });

    ScenarioBuilder escenario = scenario(nombre);
    return Parametros.consultaProductos()
        ? escenario.feed(csv(Parametros.CSV).circular()).exec(solicitud)
        : escenario.exec(solicitud);
  }

  /** Consulta de un producto. La exactitud del contador la comprueba pytest, no Gatling. */
  private static HttpRequestActionBuilder producto(String nombre) {
    return http(nombre).get("/productos/#{id}")
        .check(
            status().is(200),
            // isEL evalúa #{id}; is("#{id}") compararía contra el texto literal.
            jsonPath("$.id").isEL("#{id}"),
            jsonPath("$.nombre").exists(),
            jsonPath("$.categoria").exists(),
            jsonPath("$.precio").exists(),
            jsonPath("$.visitas").exists());
  }

  /** Respuesta mínima, sin base de datos, para comprobar que el generador sostiene la tasa. */
  private static HttpRequestActionBuilder salud(String nombre) {
    return http(nombre).get("/salud").check(status().is(200));
  }
}
