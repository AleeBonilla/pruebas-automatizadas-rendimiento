"""Inserta la sección 6 en «Documento de investigación.docx».

Convierte el borrador con pandoc usando el propio documento como referencia
de estilos, y añade al documento: la sección, las Figuras 4 y 5, las entradas
del índice y las tres referencias nuevas. Uso:
    python -I insertar.py <docx_original> <carpeta_trabajo> <docx_salida> [paginas.json]
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
BORRADOR = RAIZ / "Investigación/Secciones/06 Propuesta de taller práctico/03 Borrador.md"

# ---------------------------------------------------------------- Markdown
txt = BORRADOR.read_text(encoding="utf8")
txt = txt.split("\n---\n")[0]                      # sin el anexo C
figuras = {
    "FIGURA 4": ("Figura 4. Arquitectura del entorno del taller.", "fig4.png",
                 "elaboración propia."),
    "FIGURA 5": ("Figura 5. p95 de cada ejecución de validación frente al umbral.", "fig5.png",
                 "elaboración propia con los valores individuales de las tres campañas de validación "
                 "(`Taller/Taller.md` §7.2)."),
}
salida = []
for linea in txt.splitlines():
    s = linea.strip()
    m = re.match(r"<!-- (FIGURA \d):", s)
    if m:
        cap, img, fuente = figuras[m.group(1)]
        salida += ['::: {custom-style="TableCaption"}', cap, ":::", "",
                   '::: {custom-style="Figure"}', f"![]({img})", ":::", "",
                   '::: {custom-style="Notadetabla"}', f"*Fuente:* {fuente}", ":::", ""]
        continue
    if s.startswith("<!--"):
        continue
    linea = re.sub(r"\s*<!--.*?-->", "", linea)
    m = re.match(r"\*\*(Tabla \d\.)\*\* (.*)", linea)
    if m:
        salida += ['::: {custom-style="TableCaption"}', f"{m.group(1)} {m.group(2)}", ":::"]
        continue
    if linea.startswith("*Fuente:*"):
        salida += ['::: {custom-style="Notadetabla"}', linea, ":::"]
        continue
    salida.append(linea)
md = "\n".join(salida)
md = md.replace("# 06 Propuesta de taller práctico", "# 6. Propuesta de taller práctico")
md = md.replace("(https://github.com/AleeBonilla/pruebas-automatizadas-rendimiento)",
                "(<https://github.com/AleeBonilla/pruebas-automatizadas-rendimiento>)")
# La Figura 5 va antes de la Tabla 6: así la figura llena la página en que empieza
# la subsección y la tabla se acomoda después, sin dejar huecos.
CAP = '::: {custom-style="TableCaption"}' + chr(10)
f5 = md.index(CAP + "Figura 5.")
f5_fin = md.index(":::" + chr(10), md.index('custom-style="Notadetabla"', f5)) + 4
bloque5 = md[f5:f5_fin]
md = md[:f5] + md[f5_fin:]
t6 = md.index(CAP + "Tabla 6.")
md = md[:t6] + bloque5 + chr(10) + md[t6:]

# Tabla 6: se quita la columna «Veredictos esperados» (todas las filas dicen «Sí» y el texto lo
# afirma), para que las demás columnas no se partan, y se ajustan los anchos relativos.
t6 = md.index(CAP + "Tabla 6.")
ini = md.index("|", t6)
fin = md.index(chr(10) + chr(10), ini)
filas = md[ini:fin].split(chr(10))
assert "Veredictos esperados" in filas[0]
filas = [f[:f.rstrip().rstrip("|").rfind("|") + 1] for f in filas]
filas[1] = "|" + "|".join(["-" * 24, "-" * 15, "-" * 9 + ":", "-" * 15 + ":", "-" * 15 + ":",
                           "-" * 16 + ":", "-" * 11 + ":"]) + "|"
md = md[:ini] + chr(10).join(filas) + md[fin:]
TRAB.mkdir(parents=True, exist_ok=True)
(TRAB / "sec6.md").write_text(md, encoding="utf8")
shutil.copy(ORIG, TRAB / "ref.docx")
subprocess.run(["pandoc", "sec6.md", "-f", "markdown", "-t", "docx", "--reference-doc=ref.docx",
                "-o", "sec6.docx"], cwd=TRAB, check=True)

# ---------------------------------------------------------------- Fragmento
with zipfile.ZipFile(TRAB / "sec6.docx") as z:
    pd = z.read("word/document.xml").decode("utf8")
    prels = z.read("word/_rels/document.xml.rels").decode("utf8")
frag = pd[pd.index("<w:body>") + 8:pd.rindex("<w:sectPr")]

with zipfile.ZipFile(ORIG) as z:
    doc = z.read("word/document.xml").decode("utf8")
    rels = z.read("word/_rels/document.xml.rels").decode("utf8")
    contenido = {n: z.read(n) for n in z.namelist()}

# Relaciones: se reasignan los identificadores del fragmento.
rid_max = max(int(i) for i in re.findall(r'Id="rId(\d+)"', rels))
nuevas = []
mapa = {}
usados = set(re.findall(r'r:(?:id|embed)="(rId\d+)"', frag))
for m in re.finditer(r"<Relationship ([^>]*?)/>", prels):
    attrs = dict(re.findall(r'(\w+)="([^"]*)"', m.group(1)))
    if attrs["Id"] not in usados:
        continue
    tipo = attrs["Type"].rsplit("/", 1)[1]
    if tipo not in ("image", "hyperlink"):
        continue
    rid_max += 1
    nuevo = f"rId{rid_max}"
    mapa[attrs["Id"]] = nuevo
    if tipo == "image":
        origen = attrs["Target"]
        destino = f"media/image{rid_max}.png"
        contenido["word/" + destino] = (TRAB / Path(origen).name).read_bytes() if (TRAB / Path(origen).name).exists() \
            else zipfile.ZipFile(TRAB / "sec6.docx").read("word/" + origen)
        nuevas.append(f'<Relationship Id="{nuevo}" Type="{attrs["Type"]}" Target="{destino}"/>')
    else:
        nuevas.append(f'<Relationship Id="{nuevo}" Type="{attrs["Type"]}" Target="{attrs["Target"]}" TargetMode="External"/>')
frag = re.sub(r'r:(id|embed)="(rId\d+)"', lambda m: f'r:{m.group(1)}="{mapa[m.group(2)]}"', frag)

def juntar(m):
    t = m.group(0)
    filas = re.split(r"(?=<w:tr[ >])", t)
    for i in range(1, len(filas) - 1):
        filas[i] = filas[i].replace('<w:pStyle w:val="Compact" />', '<w:pStyle w:val="Compact" /><w:keepNext />')
    return "".join(filas)


frag = re.sub(r"<w:tbl>.*?</w:tbl>", juntar, frag, flags=re.S)

# Marcadores: se quitan los de pandoc y se ponen los del índice.
frag = re.sub(r"<w:bookmarkStart [^>]*/>|<w:bookmarkEnd [^>]*/>", "", frag)
toc_ids = {}
n_marca = [100]


def marcar(m):
    estilo, resto = m.group(1), m.group(2)
    t = re.sub(r"<[^>]+>", "", resto)
    nombre = f"_Toc2449919{20 + len(toc_ids)}"
    toc_ids[nombre] = (estilo, t)
    i = n_marca[0]
    n_marca[0] += 1
    return (f'<w:p><w:pPr><w:pStyle w:val="{estilo}"/></w:pPr><w:bookmarkStart w:id="{i}" w:name="{nombre}"/>'
            f'{resto}<w:bookmarkEnd w:id="{i}"/></w:p>')


frag = re.sub(r'<w:p>\s*<w:pPr><w:pStyle w:val="(Ttulo[12])"\s*/></w:pPr>(.*?)</w:p>', marcar, frag, flags=re.S)
assert len(toc_ids) == 8, toc_ids

frag = frag.replace("<a:graphic>", '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">')
frag = frag.replace("<pic:pic>", '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">')
ALT = {
    "fig4.png": "Diagrama de la arquitectura del entorno: Gatling envía solicitudes HTTP a la API, que consulta PostgreSQL con 2 ms de latencia; Prometheus lee las métricas de la API y Grafana consulta a Prometheus; pytest prueba la API y PostgreSQL; los scripts y GitHub Actions controlan todos los servicios.",
    "fig5.png": "Diagrama de puntos del p95 de cada ejecución de validación, en escala logarítmica. En las tres campañas, las ejecuciones de corregida quedan entre 8 y 114 ms, por debajo del umbral, y las de regresion entre 54,1 y 60 s, por encima.",
}
for nombre, alt in ALT.items():
    frag = frag.replace(f'descr="{nombre}"', f'descr="{alt}"')
frag = frag.replace('<wp:docPr descr="" title="" ', '<wp:docPr ')

# Identificadores únicos de los dibujos
id_dibujo = [max(int(i) for i in re.findall(r'<wp:docPr id="(\d+)"', doc)) + 1]


def dibujo(m):
    v = id_dibujo[0]
    id_dibujo[0] += 2
    return m.group(0).replace(m.group(1), str(v), 1)


frag = re.sub(r'<wp:docPr id="(\d+)"', dibujo, frag)
frag = re.sub(r'<pic:cNvPr id="\d+"', lambda m: f'<pic:cNvPr id="{id_dibujo[0] - 1}"', frag)

# ---------------------------------------------------------------- Cuerpo
salto = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
ref_h = re.search(r'<w:p [^>]*><w:pPr><w:pStyle w:val="Ttulo1"/></w:pPr>(?:(?!</w:p>).)*>Referencias<', doc)
assert ref_h
# el salto de página que precede a «Referencias»
i_salto = doc.rfind('<w:p ', 0, ref_h.start())
assert 'w:br w:type="page"' in doc[i_salto:ref_h.start()]
doc = doc[:i_salto] + salto + frag + doc[i_salto:]

# ---------------------------------------------------------------- Índice
def entrada(estilo, texto, ancla, pagina):
    es1 = estilo == "Ttulo1"
    ppr_extra = '<w:b w:val="0"/><w:bCs w:val="0"/>' if es1 else ""
    sty = "TDC1" if es1 else "TDC2"
    nr = '<w:rPr><w:noProof/><w:webHidden/></w:rPr>'
    return (f'<w:p><w:pPr><w:pStyle w:val="{sty}"/><w:rPr><w:rFonts w:asciiTheme="minorHAnsi" w:eastAsiaTheme="minorEastAsia" '
            f'w:hAnsiTheme="minorHAnsi" w:cstheme="minorBidi"/>{ppr_extra}<w:noProof/><w:kern w:val="2"/>'
            f'<w:lang w:val="en-US" w:eastAsia="en-US"/><w14:ligatures w14:val="standardContextual"/></w:rPr></w:pPr>'
            f'<w:hyperlink w:anchor="{ancla}" w:history="1"><w:r><w:rPr><w:rStyle w:val="Hipervnculo"/><w:noProof/></w:rPr>'
            f'<w:t>{texto}</w:t></w:r><w:r>{nr}<w:tab/></w:r><w:r>{nr}<w:fldChar w:fldCharType="begin"/></w:r>'
            f'<w:r>{nr}<w:instrText xml:space="preserve"> PAGEREF {ancla} \\h </w:instrText></w:r><w:r>{nr}</w:r>'
            f'<w:r>{nr}<w:fldChar w:fldCharType="separate"/></w:r><w:r>{nr}<w:t>{pagina}</w:t></w:r>'
            f'<w:r>{nr}<w:fldChar w:fldCharType="end"/></w:r></w:hyperlink></w:p>')


entradas = "".join(entrada(e, t, a, PAGINAS.get(a, "0")) for a, (e, t) in toc_ids.items())
k = doc.index('<w:hyperlink w:anchor="_Toc244991919"')
k = doc.rfind("<w:p ", 0, k)
doc = doc[:k] + entradas + doc[k:]
if "_Toc244991919" in PAGINAS:   # página de «Referencias»
    pat = r'(PAGEREF _Toc244991919 \\h </w:instrText></w:r><w:r><w:rPr><w:noProof/><w:webHidden/></w:rPr></w:r><w:r><w:rPr><w:noProof/><w:webHidden/></w:rPr><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:rPr><w:noProof/><w:webHidden/></w:rPr><w:t>)\d+'
    doc, n = re.subn(pat, lambda m: m.group(1) + str(PAGINAS["_Toc244991919"]), doc, count=1)
    assert n == 1

# ---------------------------------------------------------------- Referencias
nuevas_ref = [
    ("Docker Inc. (s. f.). ", "Docker Compose", ". Docker Docs. Recuperado el 10 de noviembre de 2026, de ",
     "https://docs.docker.com/compose/", "Friedrich, S."),
    ("GitHub. (s. f.). ", "Understanding GitHub Actions", ". GitHub Docs. Recuperado el 10 de noviembre de 2026, de ",
     "https://docs.github.com/en/actions/get-started/understand-github-actions", "Grafana Labs. (2026)"),
    ("Prometheus Authors. (s. f.). ", "Overview", ". Prometheus. Recuperado el 10 de noviembre de 2026, de ",
     "https://prometheus.io/docs/introduction/overview/", "Schroeder, B."),
]
for pre, tit, med, url, antes_de in nuevas_ref:
    rid_max += 1
    rid = f"rId{rid_max}"
    nuevas.append(f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" '
                  f'Target="{url}" TargetMode="External"/>')
    p = ('<w:p><w:pPr><w:pStyle w:val="Bibliografa"/></w:pPr>'
         f'<w:r><w:t xml:space="preserve">{pre}</w:t></w:r><w:r><w:rPr><w:i/><w:iCs/></w:rPr><w:t>{tit}</w:t></w:r>'
         f'<w:r><w:t xml:space="preserve">{med}</w:t></w:r><w:hyperlink r:id="{rid}"><w:r><w:rPr><w:rStyle w:val="Hipervnculo"/></w:rPr>'
         f'<w:t>{url}</w:t></w:r></w:hyperlink></w:p>')
    j = doc.index(antes_de)
    j = doc.rfind("<w:p ", 0, j)
    assert 'w:val="Bibliografa"' in doc[j:j + 200]
    doc = doc[:j] + p + doc[j:]

rels = rels.replace("</Relationships>", "".join(nuevas) + "</Relationships>")
contenido["word/document.xml"] = doc.encode("utf8")
contenido["word/_rels/document.xml.rels"] = rels.encode("utf8")
with zipfile.ZipFile(SALIDA, "w", zipfile.ZIP_DEFLATED) as z:
    with zipfile.ZipFile(ORIG) as zo:
        for info in zo.infolist():
            z.writestr(info.filename, contenido[info.filename])
    for n, b in contenido.items():
        if n not in zo.namelist():
            z.writestr(n, b)
print("listo", SALIDA, list(toc_ids.items()))
