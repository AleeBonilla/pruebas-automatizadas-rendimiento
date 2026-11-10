package taller.rendimiento;

import static io.gatling.javaapi.core.CoreDsl.*;

import io.gatling.javaapi.core.Simulation;

/**
 * Pico (Taller.md §6.3): base a TASA durante CALENTAMIENTO_S, subida abrupta a
 * PICO_TASA durante PICO_S y regreso a TASA durante MEDICION_S, que es la
 * ventana de observación de la recuperación. Las tres fases se inyectan sin
 * pausas entre ellas. No tiene aserciones: el resultado es informativo, y la
 * recuperación la calculan las herramientas con la serie por bloques (§6.4).
 */
public class PicosSimulation extends Simulation {

  private final Fases fases = new Fases();

  {
    if (Parametros.PICO_TASA <= 0) {
      throw new IllegalArgumentException("falta la tasa del pico (-DpicoTasa)");
    }
    int baseS = Parametros.CALENTAMIENTO_S;
    setUp(
        Escenarios.consulta("base", fases.fase("base", Parametros.TASA, baseS))
            .injectOpen(constantUsersPerSec(Parametros.TASA).during(baseS)),
        Escenarios.consulta("pico", fases.fase("pico", Parametros.PICO_TASA, Parametros.PICO_S))
            .injectOpen(nothingFor(baseS), constantUsersPerSec(Parametros.PICO_TASA).during(Parametros.PICO_S)),
        Escenarios.consulta("recuperacion", fases.fase("recuperacion", Parametros.TASA, Parametros.MEDICION_S))
            .injectOpen(
                nothingFor(baseS + Parametros.PICO_S),
                constantUsersPerSec(Parametros.TASA).during(Parametros.MEDICION_S)))
        .protocols(Escenarios.protocolo());
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
