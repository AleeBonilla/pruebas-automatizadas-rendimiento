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
        Escenarios.consulta("calentamiento", fases.fase("calentamiento", Parametros.TASA, Parametros.CALENTAMIENTO_S))
            .injectOpen(constantUsersPerSec(Parametros.TASA).during(Parametros.CALENTAMIENTO_S))
            // andThen: la medición empieza cuando terminan los usuarios del calentamiento.
            // Con una variante saturada, eso deja un hueco sin llegadas en el que la
            // fila se vacía; se mantiene mientras rija perfil-ci-v1 (Taller.md §6.3).
            .andThen(
                Escenarios.consulta("medicion", fases.fase("medicion", Parametros.TASA, Parametros.MEDICION_S))
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
