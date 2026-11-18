package taller.rendimiento;

import java.util.function.LongSupplier;

/** Duraciones monotónicas y UTC proyectado desde un único punto de referencia. */
final class Reloj {
  private final LongSupplier nanos;
  private final LongSupplier utc;
  private final long origenNanos;
  private final long origenUtc;

  Reloj() {
    this(System::nanoTime, System::currentTimeMillis);
  }

  Reloj(LongSupplier nanos, LongSupplier utc) {
    this.nanos = nanos;
    this.utc = utc;
    origenUtc = utc.getAsLong();
    origenNanos = nanos.getAsLong();
  }

  long ahora() {
    return nanos.getAsLong() - origenNanos;
  }

  long utcMs(long instanteNanos) {
    return origenUtc + instanteNanos / 1_000_000;
  }

  long desajusteMs() {
    return utc.getAsLong() - utcMs(ahora());
  }
}
