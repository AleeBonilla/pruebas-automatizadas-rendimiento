---
name: auditor
description: Audita el borrador de una sección y su registro de evidencia. Verifica las citas contra las fuentes y revisa la prosa contra la guía de redacción. Entrega un informe con veredicto y no corrige nada.
---

# auditor

Antes de ejecutar esta skill, leé y seguí las instrucciones de
[la skill original](../../../.claude/skills/auditor/SKILL.md).

Las rutas del documento original se resuelven desde la raíz del repositorio.
Cuando mencione `$ARGUMENTS`, usá el encargo y la sección indicados por el usuario
al invocar esta skill. Si falta la sección y no se puede inferir, preguntala,
salvo que se ejecute sin intervención humana (`codex exec`): en ese caso, registrá el problema en el informe y terminá.
