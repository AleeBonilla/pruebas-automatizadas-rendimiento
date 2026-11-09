# Reglas de Git del taller

Estas reglas se aplican a los cambios en `Taller/` y `.github/`. El documento de investigación conserva su propio flujo (no tiene).

## Ramas

- `main` contiene siempre código que pasa la compuerta. Los cambios del taller no se suben directo a `main`: entran por *pull request*.
- Cada tarea de [`Taller.md`](Taller.md) §11 se trabaja en su propia rama, creada desde `main` actualizada:

  ```text
  <tipo>/<tarea>-<descripcion>
  feat/t3-variantes-api · fix/t4-prueba-concurrencia · docs/t9-guia
  ```

  En minúsculas, con guiones y sin tildes ni ñ. Si el cambio no corresponde a una tarea, se omite el ID: `fix/healthcheck-postgres`.
- Cada rama corresponde a una tarea y a un *pull request*. Una tarea grande se divide en varios.
- `demo/regresion` y `demo/corregida` existen solo para los *pull requests* de demostración de la compuerta (`Taller.md` §8). Esos *pull requests* no se integran.

## Commits

```text
<tipo>(<ámbito>): <descripción>

<cuerpo opcional: qué cambia y por qué>

Tarea: T3
```

- **Descripción:** en español, en infinitivo, con minúscula inicial, sin punto final y con un máximo de 72 caracteres. Ejemplo: `feat(api): agregar la variante corregida con UPDATE atómico`.
- **Tipos:**

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
- Cada commit hace una sola cosa y deja el proyecto funcionando. Una refactorización no va en el mismo commit que un cambio de comportamiento.
- Una vez congelado un perfil, cambiar versiones, la configuración de `Taller.md` §5.2, los datos semilla, las variantes o la simulación cambia el sistema medido. Ese cambio va en un commit propio, con la línea `Invalida: perfil-<entorno>-v<n>` al pie.

## Pull requests

- El título sigue el formato de los commits. La integración se hace con *squash merge*, así que el título pasa a ser el commit de `main`. Para eso, el repositorio usa el título y la descripción del *pull request* como mensaje predeterminado.
- La descripción indica qué cambia, cómo se probó y qué tarea cierra (`Tarea: T3`).
- Para integrar, la compuerta debe pasar y la otra persona del equipo debe aprobar la revisión. Nadie integra su propio *pull request* sin esa aprobación.
- Para traer cambios de `main` a la rama se usa `git merge origin/main`; el *squash* deja limpio el historial.
- Después de integrar, la rama se borra.

## Etiquetas

Al congelar un perfil se crea una etiqueta anotada en el commit con el que se calibró: `perfil-local-v1`, `perfil-ci-v1`. Cada validación se ejecuta sobre ese commit o sobre uno posterior que no lo invalide, y la carpeta de resultados registra la revisión usada.

## Archivos

- No se versionan los resultados de las ejecuciones (`resultados/`), los compilados (`target/`), las cachés de Python ni los entornos virtuales ni la configuración local de los editores (ver `.gitignore`).
- Los perfiles `config/perfiles/*.env` sí se versionan, porque no contienen secretos. El repositorio no guarda credenciales; si hicieran falta, irían en los *secrets* de GitHub Actions.
- `.gitattributes` fuerza finales de línea LF en `*.sh` y `mvnw`. Con CRLF, generado por Git en Windows, esos scripts fallan dentro de los contenedores y en el *runner* de Linux.
