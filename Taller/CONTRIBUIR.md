# Reglas de Git del taller

Estas convenciones se aplican a los cambios en `Taller/` y `.github/`. El documento de investigación sigue su propio flujo.

## Flujo de trabajo

- Por defecto se trabaja directamente sobre `main`: cada persona confirma sus cambios y los sube con `git push`.
- Cuando hace falta, se usa una rama y un *pull request*: por ejemplo, para que la compuerta corra antes de integrar o para que la otra persona vea un cambio en archivos compartidos. La rama se llama `<tipo>/<tarea>-<descripcion>` (`feat/t10-estres-picos`), el *pull request* se integra con *squash merge* y su título sigue el formato de los commits.
- Antes de subir, `git pull --rebase` trae lo de la otra persona sin commits de *merge*. Si hay un conflicto, lo resuelve quien sube.
- Nunca se reescribe la historia de `main` (`git push --force`, `git rebase` sobre commits ya subidos).
- Cada persona toca sus propios archivos (`Taller.md` §11). Si un cambio toca los de la otra o los compartidos (`compose.yaml`, `config/` o los acuerdos de §11), se le avisa antes de subirlo.
- La compuerta corre en cada *push* a `main`. Si queda en rojo, quien subió el cambio lo arregla o lo revierte con `git revert` antes de seguir.
- Para probar algo que podría romper la compuerta, se puede usar una rama `prueba/<descripcion>` y correr la compuerta sobre ella con `gh workflow run compuerta.yml --ref prueba/<descripcion>`. Cuando funciona, se lleva a `main` y se borra la rama.
- `demo/regresion` y `demo/corregida` siempre van con *pull request*, porque la demostración de la compuerta los necesita (`Taller.md` §8). Esos *pull requests* no se integran.

## Commits

```text
<tipo>(<ámbito>): <descripción>

<cuerpo opcional>

Tarea: T3
```

- **Descripción:** en español, en infinitivo, con minúscula inicial, sin punto final y con un máximo de 72 caracteres. Ejemplo: `feat(api): agregar la variante corregida con UPDATE atómico`.
- La línea `Tarea:` se omite si el cambio no corresponde a una tarea.

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
