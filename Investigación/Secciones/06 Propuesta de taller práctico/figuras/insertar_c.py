"""Agrega el anexo C al final de «Documento de investigación.docx» (después de las referencias).
Uso: python -I insertar_c.py <docx_entrada> <carpeta_trabajo> <docx_salida> [paginas.json]
"""
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ORIG, TRAB, SALIDA = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
PAGINAS = json.loads(Path(sys.argv[4]).read_text(encoding="utf8")) if len(sys.argv) > 4 else {}
RAIZ = Path(r"C:/Users/abofi/alee's stuff/Resources/TEC/Aseguramiento de la Calidad del Software/pruebas-automatizadas-rendimiento")
SEC = RAIZ / "Investigación/Secciones/06 Propuesta de taller práctico"
NL = chr(10)

# ---------------------------------------------------------------- Markdown
txt = (SEC / "03 Borrador.md").read_text(encoding="utf8").replace(chr(13) + NL, NL)
txt = txt[txt.index("## Anexo C."):]
sal = []
for linea in txt.splitlines():
    s = linea.strip()
    if s.startswith("<!-- FIGURA 6:"):
        sal += ['::: {custom-style="TableCaption"}', "Figura 6. Informe de Gatling de la medición, por variante.", ":::", "",
                '::: {custom-style="Figure"}', "![](fig6.png){width=4.8in}", ":::", "",
                '::: {custom-style="Notadetabla"}',
                "*Fuente:* elaboración propia. Ejecuciones `20261110T231112Z-carga-corregida` y "
                "`20261110T230416Z-carga-regresion` de `validacion-ci-2` (*runner* de GitHub Actions, 10 de noviembre de 2026).", ":::", ""]
        continue
    if s.startswith("<!--"):
        continue
    if s.startswith("*Fuente:*"):
        sal += ['::: {custom-style="Notadetabla"}', linea, ":::"]
        continue
    sal.append(linea)
md = NL.join(sal)
md = md.replace("## Anexo C. Material del taller", "# Anexo C. Material del taller")
md = re.sub(r"^### (C\.\d)", r"## \1", md, flags=re.M)
md = md.replace("El taller está en https://github.com/AleeBonilla/pruebas-automatizadas-rendimiento, carpeta",
                "El taller está en <https://github.com/AleeBonilla/pruebas-automatizadas-rendimiento>, carpeta")
assert md.count("fig6.png") == 1
TRAB.mkdir(parents=True, exist_ok=True)
(TRAB / "anexoc.md").write_text(md, encoding="utf8")
shutil.copy(SEC / "figuras/fig6.png", TRAB / "fig6.png")
shutil.copy(ORIG, TRAB / "ref_c.docx")
subprocess.run(["pandoc", "anexoc.md", "-f", "markdown", "-t", "docx", "--reference-doc=ref_c.docx",
                "-o", "anexoc.docx"], cwd=TRAB, check=True)

# ---------------------------------------------------------------- Fragmento
with zipfile.ZipFile(TRAB / "anexoc.docx") as z:
    pd = z.read("word/document.xml").decode("utf8")
    prels = z.read("word/_rels/document.xml.rels").decode("utf8")
    pmedia = {n: z.read(n) for n in z.namelist() if n.startswith("word/media/")}
frag = pd[pd.index("<w:body>") + 8:pd.rindex("<w:sectPr")]

with zipfile.ZipFile(ORIG) as z:
    doc = z.read("word/document.xml").decode("utf8")
    rels = z.read("word/_rels/document.xml.rels").decode("utf8")
    contenido = {n: z.read(n) for n in z.namelist()}

rid_max = max(int(i) for i in re.findall(r'Id="rId(\d+)"', rels))
nuevas, mapa = [], {}
usados = set(re.findall(r'r:(?:id|embed)="(rId\d+)"', frag))
for m in re.finditer(r"<Relationship ([^>]*?)/>", prels):
    a = dict(re.findall(r'(\w+)="([^"]*)"', m.group(1)))
    if a["Id"] not in usados:
        continue
    tipo = a["Type"].rsplit("/", 1)[1]
    rid_max += 1
    nuevo = f"rId{rid_max}"
    mapa[a["Id"]] = nuevo
    if tipo == "image":
        destino = f"media/image{rid_max}.png"
        contenido["word/" + destino] = pmedia["word/" + a["Target"]]
        nuevas.append(f'<Relationship Id="{nuevo}" Type="{a["Type"]}" Target="{destino}"/>')
    else:
        nuevas.append(f'<Relationship Id="{nuevo}" Type="{a["Type"]}" Target="{a["Target"]}" TargetMode="External"/>')
frag = re.sub(r'r:(id|embed)="(rId\d+)"', lambda m: f'r:{m.group(1)}="{mapa[m.group(2)]}"', frag)

frag = re.sub(r"<w:bookmarkStart [^>]*/>|<w:bookmarkEnd [^>]*/>", "", frag)
ult_marca = max(int(i) for i in re.findall(r'<w:bookmarkStart w:id="(\d+)"', doc))
ult_toc = max(int(i) for i in re.findall(r"_Toc(\d+)", doc))
toc_ids = {}
cont = [ult_marca + 1]


def marcar(m):
    estilo, resto = m.group(1), m.group(2)
    texto = re.sub(r"<[^>]+>", "", resto)
    nombre = f"_Toc{ult_toc + 1 + len(toc_ids)}"
    toc_ids[nombre] = (estilo, texto)
    i = cont[0]
    cont[0] += 1
    return (f'<w:p><w:pPr><w:pStyle w:val="{estilo}"/></w:pPr><w:bookmarkStart w:id="{i}" w:name="{nombre}"/>'
            f'{resto}<w:bookmarkEnd w:id="{i}"/></w:p>')


frag = re.sub(r'<w:p>\s*<w:pPr><w:pStyle w:val="(Ttulo[12])"\s*/></w:pPr>(.*?)</w:p>', marcar, frag, flags=re.S)
assert len(toc_ids) == 5, toc_ids

frag = frag.replace('<w:pPr><w:pStyle w:val="Figure" /></w:pPr>', '<w:pPr><w:pStyle w:val="Figure" /><w:keepNext /></w:pPr>')
frag = frag.replace("<a:graphic>", '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">')
frag = frag.replace("<pic:pic>", '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">')
ALT = ("Capturas de la página de la medición del informe de Gatling en dos ejecuciones con el perfil ci. "
       "En corregida, el p50 es de 7 ms, el p95 de 8 ms, no hay errores y las respuestas siguen a las solicitudes. "
       "En regresion, el p50 es de 24,0 s, el p95 de 59,1 s y hay 18,8 % de errores.")
frag = frag.replace('descr="fig6.png"', f'descr="{ALT}"')
frag = frag.replace('<wp:docPr descr="" title="" ', "<wp:docPr ")
sig = max(int(i) for i in re.findall(r'<wp:docPr id="(\d+)"', doc)) + 1
frag = re.sub(r'<wp:docPr id="\d+"', f'<wp:docPr id="{sig}"', frag)
frag = re.sub(r'<pic:cNvPr id="\d+"', f'<pic:cNvPr id="{sig + 1}"', frag)

# ---------------------------------------------------------------- Cuerpo: al final del documento
salto = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
k = doc.rindex("<w:sectPr")
doc = doc[:k] + salto + frag + doc[k:]


# ---------------------------------------------------------------- Índice
def entrada(estilo, texto, ancla, pagina):
    es1 = estilo == "Ttulo1"
    extra = '<w:b w:val="0"/><w:bCs w:val="0"/>' if es1 else ""
    sty = "TDC1" if es1 else "TDC2"
    nr = "<w:rPr><w:noProof/><w:webHidden/></w:rPr>"
    return (f'<w:p><w:pPr><w:pStyle w:val="{sty}"/><w:rPr><w:rFonts w:asciiTheme="minorHAnsi" w:eastAsiaTheme="minorEastAsia" '
            f'w:hAnsiTheme="minorHAnsi" w:cstheme="minorBidi"/>{extra}<w:noProof/><w:kern w:val="2"/>'
            f'<w:lang w:val="en-US" w:eastAsia="en-US"/><w14:ligatures w14:val="standardContextual"/></w:rPr></w:pPr>'
            f'<w:hyperlink w:anchor="{ancla}" w:history="1"><w:r><w:rPr><w:rStyle w:val="Hipervnculo"/><w:noProof/></w:rPr>'
            f'<w:t>{texto}</w:t></w:r><w:r>{nr}<w:tab/></w:r><w:r>{nr}<w:fldChar w:fldCharType="begin"/></w:r>'
            f'<w:r>{nr}<w:instrText xml:space="preserve"> PAGEREF {ancla} \\h </w:instrText></w:r><w:r>{nr}</w:r>'
            f'<w:r>{nr}<w:fldChar w:fldCharType="separate"/></w:r><w:r>{nr}<w:t>{pagina}</w:t></w:r>'
            f'<w:r>{nr}<w:fldChar w:fldCharType="end"/></w:r></w:hyperlink></w:p>')


entradas = "".join(entrada(e, t, a, PAGINAS.get(a, "0")) for a, (e, t) in toc_ids.items())
ancla_ref = '<w:hyperlink w:anchor="_Toc244991919"'
j = doc.index(ancla_ref)
j = doc.index("</w:p>", j) + 6
doc = doc[:j] + entradas + doc[j:]

# El índice ahora ocupa casi toda la página 2: se quita el párrafo vacío que cierra el campo y el salto de
# página suelto que le sigue, para que no rebosen a una página en blanco. El campo se cierra en la última
# entrada, y el salto pasa a ser un «salto de página antes» del título de la introducción.
m_fin = re.search(r'<w:p [^>]*><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p></w:sdtContent>', doc)
assert m_fin
doc = doc.replace(m_fin.group(0), "</w:sdtContent>")
k_ult = doc.rindex("</w:hyperlink></w:p>", 0, doc.index("</w:sdtContent>"))
doc = doc[:k_ult] + '</w:hyperlink><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>' + doc[k_ult + len("</w:hyperlink></w:p>"):]
m_br = re.search(r'</w:sdt><w:p [^>]*><w:r><w:br w:type="page"/></w:r></w:p>(<w:p [^>]*><w:pPr><w:pStyle w:val="Ttulo1"/>)', doc)
assert m_br
doc = doc.replace(m_br.group(0), "</w:sdt>" + m_br.group(1) + "<w:pageBreakBefore/>", 1)

rels = rels.replace("</Relationships>", "".join(nuevas) + "</Relationships>")
contenido["word/document.xml"] = doc.encode("utf8")
contenido["word/_rels/document.xml.rels"] = rels.encode("utf8")
with zipfile.ZipFile(SALIDA, "w", zipfile.ZIP_DEFLATED) as z:
    with zipfile.ZipFile(ORIG) as zo:
        orden = zo.namelist()
    for n in orden:
        z.writestr(n, contenido[n])
    for n, b in contenido.items():
        if n not in orden:
            z.writestr(n, b)
print("listo", [(a, t) for a, (e, t) in toc_ids.items()])
