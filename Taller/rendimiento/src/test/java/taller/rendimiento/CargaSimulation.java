package taller.rendimiento;

import static io.gatling.javaapi.core.CoreDsl.*;

import io.gatling.javaapi.core.Simulation;

/**
 * Prueba de carga que funciona como compuerta (Taller.md §6.2): calentamiento y
 * medición a tasa constante, con aserciones solo sobre la medición.
 */
public class CargaSimulation extends Simulation {

  private final Fases fases = new Fases();

  {
    setUp(
        Escenarios.consulta("calentamiento", fases.fase("calentamiento"))
            .injectOpen(constantUsersPerSec(Parametros.TASA).during(Parametros.CALENTAMIENTO_S))
            // andThen: la medición empieza cuando terminan los usuarios del calentamiento.
            .andThen(
                Escenarios.consulta("medicion", fases.fase("medicion"))
                    .injectOpen(constantUsersPerSec(Parametros.TASA).during(Parametros.MEDICION_S))))
        .protocols(Escenarios.protocolo())
        .assertions(
            details("medicion").responseTime().percentile(95.0).lt(Parametros.UMBRAL_MS),
            details("medicion").failedRequests().percent().lte(Parametros.ERRORES_MAX_PCT));
  }

  @Override
  public void before() {
    fases.iniciarSimulacion();
  }

  @Override
  public void after() {
    fases.escribir(getClass().getSimpleName());
  }
}
