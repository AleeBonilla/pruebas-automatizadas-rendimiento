package taller.rendimiento;

import java.util.concurrent.atomic.AtomicLong;

/** Regresión determinista: saltos UTC hacia delante y atrás durante una fase. */
public final class RelojPrueba {
  public static void main(String[] args) {
    for (long salto : new long[] {1_500, -5_000}) {
      AtomicLong ns = new AtomicLong(100_000_000_000L);
      AtomicLong utc = new AtomicLong(1_700_000_000_000L);
      Reloj reloj = new Reloj(ns::get, utc::get);
      Fases.Fase fase = new Fases.Fase(20, 60, reloj);
      long inicio = fase.marcarInicio();
      ns.addAndGet(10_000_000);
      utc.addAndGet(10 + salto);
      fase.marcarFin(inicio, false);
      ns.addAndGet(59_940_000_000L);
      utc.addAndGet(59_940);
      inicio = fase.marcarInicio();
      ns.addAndGet(10_000_000);
      utc.addAndGet(10);
      fase.marcarFin(inicio, false);
      String json = fase.json();
      for (String esperado : new String[] {
          "\"inyeccion_s\": 59.950", "\"duracion_s\": 59.960",
          "\"desde_s\": 55", "\"max_ms\": 10", "\"terminadas\": 2"}) {
        if (!json.contains(esperado)) throw new AssertionError(json);
      }
      if (reloj.desajusteMs() != salto) throw new AssertionError("desajuste UTC");
    }
    System.out.println("RelojPrueba: saltos UTC positivos y negativos verificados");
  }
}
