---
name: planificador
description: Planifica una sección de un documento de investigación. Define su modo, su esquema argumental y sus fuentes. No redacta la sección.
---

# planificador

Antes de ejecutar esta skill, leé y seguí las instrucciones de
[la skill original](../../../.claude/skills/planificador/SKILL.md).

Las rutas del documento original se resuelven desde la raíz del repositorio.
Cuando mencione `$ARGUMENTS`, usá el encargo y la sección indicados por el usuario
al invocar esta skill. Si falta la sección y no se puede inferir, preguntala,
salvo que se ejecute sin intervención humana (`codex exec`): en ese caso, registrá el problema en el informe y terminá.
