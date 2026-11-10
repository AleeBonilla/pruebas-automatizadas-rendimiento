package taller.rendimiento;

import static io.gatling.javaapi.core.CoreDsl.*;

import io.gatling.javaapi.core.Simulation;

/**
 * Un nivel de estrés (Taller.md §6.3): calentamiento y meseta a tasa constante,
 * una ejecución por nivel. Las aserciones son las del perfil y solo dicen si ese
 * nivel cumple el criterio; el resultado es informativo, no una compuerta.
 *
 * <p>A diferencia de CargaSimulation, la medición no espera a que terminen los
 * usuarios del calentamiento: empieza a la hora prevista, así la llegada es
 * continua y una variante saturada entra a la meseta con la fila que ya formó.
 */
public class EstresSimulation extends Simulation {

  private final Fases fases = new Fases();

  {
    setUp(
        Escenarios.consulta("calentamiento", fases.fase("calentamiento", Parametros.TASA, Parametros.CALENTAMIENTO_S))
            .injectOpen(constantUsersPerSec(Parametros.TASA).during(Parametros.CALENTAMIENTO_S)),
        Escenarios.consulta("medicion", fases.fase("medicion", Parametros.TASA, Parametros.MEDICION_S))
            .injectOpen(
                nothingFor(Parametros.CALENTAMIENTO_S),
                constantUsersPerSec(Parametros.TASA).during(Parametros.MEDICION_S)))
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
