"""Pasa al Word los cambios del borrador v3 de la sección 6: la Tabla 6 (valores de prueba) al final de 6.4
y la Tabla 7 (resultados esperados y obtenidos) en 6.6, en lugar de la antigua Tabla 6.
Uso: python -I insertar_e.py <docx_entrada> <carpeta_trabajo> <docx_salida>
"""
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ORIG, TRAB, SALIDA = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
SEC = Path(__file__).resolve().parent.parent
NL = chr(10)
CORTE = "ZZCORTEZZ"
ANCHOS = {"Tabla 6.": [28, 22, 26, 24], "Tabla 7.": [30, 30, 40]}

# ---------------------------------------------------------------- Markdown desde el borrador
txt = (SEC / "03 Borrador.md").read_text(encoding="utf8").replace(chr(13) + NL, NL)
txt = re.sub(r"<!--.*?-->", "", txt, flags=re.S)


def bloque(inicio, fin):
    """Desde la línea que empieza con `inicio` hasta la primera línea de fuente posterior (incluida)."""
    i = txt.index(inicio)
    j = txt.index("*Fuente:*", txt.index(fin, i))
    return txt[i:txt.index(NL, j)]


partes = [bloque("Como cada computadora es distinta", "**Tabla 6.**"),
          bloque("La Tabla 7 contrasta", "**Tabla 7.**")]
sal = []
for linea in (NL + NL + CORTE + NL + NL).join(partes).splitlines():
    m = re.match(r"\*\*(Tabla \d+\.)\*\* (.*)", linea)
    if m:
        sal += ['::: {custom-style="TableCaption"}', f"{m.group(1)} {m.group(2)}", ":::", ""]
    elif linea.startswith("*Fuente:*"):
        sal += ['::: {custom-style="Notadetabla"}', linea, ":::"]
    else:
        sal.append(linea)
md = NL.join(sal)
for nombre, pesos in ANCHOS.items():
    i = md.index("|", md.index(nombre))
    k = md.index(NL, i) + 1
    j = md.index(NL, k)
    md = md[:k] + "|" + "|".join("-" * p for p in pesos) + "|" + md[j:]

TRAB.mkdir(parents=True, exist_ok=True)
(TRAB / "tablas.md").write_text(md, encoding="utf8")
shutil.copy(ORIG, TRAB / "ref_e.docx")
subprocess.run(["pandoc", "tablas.md", "-f", "markdown", "-t", "docx", "--reference-doc=ref_e.docx",
                "-o", "tablas.docx"], cwd=TRAB, check=True)

with zipfile.ZipFile(TRAB / "tablas.docx") as z:
    pd = z.read("word/document.xml").decode("utf8")
frag = pd[pd.index("<w:body>") + 8:pd.rindex("<w:sectPr")]
frag = re.sub(r"<w:bookmarkStart [^>]*/>|<w:bookmarkEnd [^>]*/>", "", frag)
frag = frag.replace('<w:pStyle w:val="BodyText" />', '<w:pStyle w:val="FirstParagraph" />')
assert "r:id=" not in frag and "r:embed=" not in frag
# Ninguna fila se parte entre dos páginas.
frag = frag.replace("<w:trPr>", "<w:trPr><w:cantSplit />")
frag = re.sub(r"<w:tr>(?!<w:trPr>)", "<w:tr><w:trPr><w:cantSplit /></w:trPr>", frag)
m = re.search(r"<w:p>(?:(?!<w:p>).)*?" + CORTE + r".*?</w:p>", frag, flags=re.S)
frag_a, frag_b = frag[:m.start()], frag[m.end():]
assert "Tabla 6." in frag_a and "Tabla 7." in frag_b

# ---------------------------------------------------------------- Documento
with zipfile.ZipFile(ORIG) as z:
    contenido = {n: z.read(n) for n in z.namelist()}
    orden = z.namelist()
doc = contenido["word/document.xml"].decode("utf8")


def parrafo(texto):
    i = doc.index(texto)
    s = max(doc.rfind("<w:p>", 0, i), doc.rfind("<w:p ", 0, i))
    return s, doc.index("</w:p>", i) + 6


# 6.6: el párrafo de apertura y la antigua Tabla 6 (título, tabla y fuente)
s, e = parrafo("Las 19 ejecuciones de validaci")
frag_b1 = frag_b[:frag_b.index('<w:pStyle w:val="TableCaption" />')]
frag_b1 = frag_b1[:frag_b1.rindex("<w:p>")]
frag_b2 = frag_b[len(frag_b1):]
ts, _ = parrafo("Tabla 6. Resultados de las campa")
_, te = parrafo("Un p95 de 60 s es el l")
assert s < e < ts < te
doc = doc[:ts] + frag_b2 + doc[te:]
doc = doc[:s] + frag_b1 + doc[e:]

# 6.4: el último párrafo, seguido de la nueva Tabla 6
s, e = parrafo("Como cada computadora es distinta")
doc = doc[:s] + frag_a + doc[e:]

# 6.1: las 38 pruebas son el total de la suite, no las de cada variante
viejo = "Las dos implementaciones del contador aprueban las mismas 38 pruebas funcionales y de concurrencia"
assert doc.count(viejo) == 1
doc = doc.replace(viejo, viejo.replace("mismas 38 pruebas", "mismas pruebas"))

for viejo in ("Resultados de las campa", "resumidas en la Tabla 6"):
    assert viejo not in doc, viejo
assert doc.count("Tabla 6. Valores de prueba") == 1 and doc.count("Tabla 7. Resultados esperados") == 1

contenido["word/document.xml"] = doc.encode("utf8")
with zipfile.ZipFile(SALIDA, "w", zipfile.ZIP_DEFLATED) as z:
    for n in orden:
        z.writestr(n, contenido[n])
print("listo")
