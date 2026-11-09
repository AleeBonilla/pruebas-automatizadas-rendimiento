# Reglas de Git del taller

Estas convenciones de nombres y ramas se aplican a los cambios en `Taller/` y `.github/`. El documento de investigación sigue su propio flujo.

## Ramas

- Cada tarea de [`Taller.md`](Taller.md) §11 se trabaja en una rama propia, creada desde `main`:

  ```text
  <tipo>/<tarea>-<descripcion>
  feat/t3-variantes-api · fix/t4-prueba-concurrencia · docs/t9-guia
  ```

  En minúsculas, con guiones y sin tildes ni ñ. Si el cambio no corresponde a una tarea, se omite el ID: `fix/healthcheck-postgres`.
- Una tarea grande se puede repartir en varias ramas: `feat/t5-proyecto-gatling` y `build/t5-servicio-gatling`.
- Los cambios entran a `main` por *pull request* con *squash merge*. Cada persona integra los suyos sin esperar aprobación. Si el cambio toca archivos de la otra persona o compartidos (`compose.yaml`, `config/` o los acuerdos de §11), se la menciona en la descripción.
- `demo/regresion` y `demo/corregida` existen solo para los *pull requests* de demostración de la compuerta (`Taller.md` §8). Esos *pull requests* no se integran.

## Commits y *pull requests*

```text
<tipo>(<ámbito>): <descripción>

<cuerpo opcional>

Tarea: T3
```

- **Descripción:** en español, en infinitivo, con minúscula inicial, sin punto final y con un máximo de 72 caracteres. Ejemplo: `feat(api): agregar la variante corregida con UPDATE atómico`.
- El título del *pull request* usa el mismo formato, porque el *squash* lo convierte en el commit de `main`.

| Tipo       | Uso                                                                        |
| ---------- | -------------------------------------------------------------------------- |
| `feat`     | Funcionalidad nueva: endpoints, variantes, simulaciones, paneles, comandos |
| `fix`      | Corrección de un defecto                                                   |
| `test`     | Pruebas de pytest nuevas o corregidas, sin cambiar la API                  |
| `refactor` | Cambio de código que no altera el comportamiento                           |
| `build`    | Dockerfiles, `compose.yaml`, dependencias y versiones                      |
| `ci`       | Workflows de GitHub Actions                                                |
| `docs`     | Guías y documentación                                                      |
| `chore`    | Mantenimiento que no encaja en los anteriores                              |

- **Ámbitos:** `api`, `datos` (`base-datos/`), `rendimiento`, `observabilidad`, `config`, `herramientas` y `entorno` (`compose.yaml`, `taller.ps1`, `taller.sh`). En `ci` y `docs` el ámbito se puede omitir.

## Perfiles

- Al congelar un perfil se crea una etiqueta anotada en ese commit: `perfil-<entorno>-v<n>`, por ejemplo `perfil-local-v1` o `perfil-ci-v1`.
- Un commit posterior que cambie el sistema medido (versiones, configuración de §5.2, datos semilla, variantes o simulación) lleva al pie la línea `Invalida: perfil-<entorno>-v<n>`.

## Archivos

- `resultados/`, `target/`, las cachés y los entornos virtuales no se versionan (ver `.gitignore`). Los perfiles `config/perfiles/*.env` sí, porque no contienen secretos.
- `.gitattributes` fuerza LF en `*.sh` y `mvnw`. Con CRLF, esos scripts fallan en los contenedores y en el *runner* de Linux.
