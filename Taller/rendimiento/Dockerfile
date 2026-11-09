# Generador de carga: Gatling con el DSL de Java (Taller.md §5.1).
FROM eclipse-temurin:25.0.5_8-jdk-noble

WORKDIR /rendimiento

# Primero el Wrapper y el pom: las dependencias quedan en una capa propia y no se
# vuelven a descargar cuando solo cambian las simulaciones.
COPY mvnw pom.xml ./
COPY .mvn .mvn
RUN chmod +x mvnw && ./mvnw -B -q dependency:go-offline

COPY src src
# Compila y resuelve el classpath del plugin durante la construcción, así la
# ejecución funciona sin red (-o).
RUN ./mvnw -B -q test-compile dependency:resolve-plugins

# Los parámetros llegan como propiedades del sistema: docker compose run gatling -Dtasa=20 ...
ENTRYPOINT ["./mvnw", "-B", "-o", "gatling:test"]
CMD ["-Dgatling.simulationClass=taller.rendimiento.CargaSimulation"]
