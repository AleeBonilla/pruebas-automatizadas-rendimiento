"""Agrega al Word la sección 7 (Conclusiones) y los anexos A y B.
Uso: python -I insertar_d.py <docx_entrada> <carpeta_trabajo> <docx_salida> [medidas.json]
medidas.json: salida de medir.ps1 (título -> página); actualiza todo el índice.
"""
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ORIG, TRAB, SALIDA = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
MEDIDAS = {}
if len(sys.argv) > 4:
    MEDIDAS = json.loads(Path(sys.argv[4]).read_text(encoding="utf-8-sig"))["titulos"]
RAIZ = Path(r"C:/Users/abofi/alee's stuff/Resources/TEC/Aseguramiento de la Calidad del Software/pruebas-automatizadas-rendimiento")
SEC = RAIZ / "Investigación/Secciones"
NL = chr(10)
CAP = '::: {custom-style="TableCaption"}' + NL

# Anchos relativos (guiones) de cada tabla, en orden de aparición.
ANCHOS = {
    "Tabla A1.": [18, 38, 44],
    "Tabla A2.": [24, 9, 11, 10, 9, 11, 10],
    "Tabla B1.": [40, 15, 15, 15, 15],
    "Tabla B2.": [28, 8, 36, 28],
    "Tabla B3.": [28, 44, 28],
}


def a_markdown(ruta):
    txt = ruta.read_text(encoding="utf8").replace(chr(13) + NL, NL)
    sal = []
    for linea in txt.splitlines():
        s = linea.strip()
        if s.startswith("<!--"):
            continue
        m = re.match(r"\*\*(Tabla [A-Z]?\d+\.)\*\* (.*)", linea)
        if m:
            sal += ['::: {custom-style="TableCaption"}', f"{m.group(1)} {m.group(2)}", ":::"]
            continue
        if s.startswith("*Fuente:*"):
            sal += ['::: {custom-style="Notadetabla"}', linea, ":::"]
            continue
        sal.append(linea)
    md = NL.join(sal)
    # anchos de columna: se reescribe la línea de guiones que sigue a cada título de tabla
    for nombre, pesos in ANCHOS.items():
        i = md.find(nombre)
        if i < 0:
            continue
        i = md.index("|", i)
        j = md.index(NL, md.index(NL, i) + 1)
        sep = md[md.index(NL, i) + 1:j]
        alin = [c.strip() for c in sep.strip("|").split("|")]
        celdas = []
        for a, p in zip(alin, pesos):
            celdas.append("-" * p + (":" if a.endswith(":") else ""))
        md = md[:md.index(NL, i) + 1] + "|" + "|".join(celdas) + "|" + md[j:]
    return md


TRAB.mkdir(parents=True, exist_ok=True)
(TRAB / "concl.md").write_text(a_markdown(SEC / "07 Conclusiones/03 Borrador.md"), encoding="utf8")
(TRAB / "anexos_ab.md").write_text(a_markdown(SEC / "09 Anexos A y B/03 Borrador.md"), encoding="utf8")
shutil.copy(ORIG, TRAB / "ref_d.docx")
for n in ("concl", "anexos_ab"):
    subprocess.run(["pandoc", f"{n}.md", "-f", "markdown", "-t", "docx", "--reference-doc=ref_d.docx",
                    "-o", f"{n}.docx"], cwd=TRAB, check=True)

with zipfile.ZipFile(ORIG) as z:
    doc = z.read("word/document.xml").decode("utf8")
    rels = z.read("word/_rels/document.xml.rels").decode("utf8")
    contenido = {n: z.read(n) for n in z.namelist()}


def inicio_p(d, pos):
    return max(d.rfind("<w:p>", 0, pos), d.rfind("<w:p ", 0, pos))


def cuerpo(nombre):
    with zipfile.ZipFile(TRAB / f"{nombre}.docx") as z:
        pd = z.read("word/document.xml").decode("utf8")
    f = pd[pd.index("<w:body>") + 8:pd.rindex("<w:sectPr")]
    f = re.sub(r"<w:bookmarkStart [^>]*/>|<w:bookmarkEnd [^>]*/>", "", f)
    return f


def juntar(m):
    filas = re.split(r"(?=<w:tr[ >])", m.group(0))
    for i in range(1, min(3, len(filas) - 1)):   # solo el encabezado y la primera fila: la tabla puede partirse
        filas[i] = filas[i].replace('<w:pStyle w:val="Compact" />', '<w:pStyle w:val="Compact" /><w:keepNext />')
    for i in range(1, len(filas)):   # las filas no se parten entre páginas
        f = filas[i]
        if "<w:trPr>" in f:
            f = f.replace("<w:tblHeader", "<w:cantSplit /><w:tblHeader", 1) if "<w:tblHeader" in f else f.replace("<w:trPr>", "<w:trPr><w:cantSplit />", 1)
        else:
            f = re.sub(r"^(<w:tr[^>]*>)", lambda m: m.group(1) + "<w:trPr><w:cantSplit /></w:trPr>", f, count=1)
        filas[i] = f
    return "".join(filas)


ult_marca = max(int(i) for i in re.findall(r'<w:bookmarkStart w:id="(\d+)"', doc))
ult_toc = max(int(i) for i in re.findall(r"_Toc(\d+)", doc))
toc_ids = {}
cont = [ult_marca + 1]


def marcar(m):
    resto = m.group(1)
    texto = re.sub(r"<[^>]+>", "", resto)
    nombre = f"_Toc{ult_toc + 1 + len(toc_ids)}"
    toc_ids[nombre] = texto
    i = cont[0]
    cont[0] += 1
    return (f'<w:p><w:pPr><w:pStyle w:val="Ttulo1"/></w:pPr><w:bookmarkStart w:id="{i}" w:name="{nombre}"/>'
            f'{resto}<w:bookmarkEnd w:id="{i}"/></w:p>')


def preparar(f):
    f = re.sub(r"<w:tbl>.*?</w:tbl>", juntar, f, flags=re.S)
    return re.sub(r'<w:p>\s*<w:pPr><w:pStyle w:val="Ttulo1"\s*/></w:pPr>(.*?)</w:p>', marcar, f, flags=re.S)


f_concl = preparar(cuerpo("concl"))
f_ab = preparar(cuerpo("anexos_ab"))
assert len(toc_ids) == 3, toc_ids
nombres = list(toc_ids)

salto = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
# 1) Conclusiones: antes del salto de página que precede a «Referencias»
ref_h = re.search(r'<w:p [^>]*><w:pPr><w:pStyle w:val="Ttulo1"/></w:pPr>(?:(?!</w:p>).)*>Referencias<', doc)
i_salto = inicio_p(doc, ref_h.start())
assert 'w:br w:type="page"' in doc[i_salto:ref_h.start()]
doc = doc[:i_salto] + salto + f_concl + doc[i_salto:]
# 2) Anexos A y B: justo antes del anexo C (el salto de página previo queda delante del anexo A)
m_c = re.search(r'<w:p(?: [^>]*)?><w:pPr><w:pStyle w:val="Ttulo1"/></w:pPr><w:bookmarkStart [^>]*/>(?:(?!</w:p>).)*>Anexo C\.', doc)
assert m_c
doc = doc[:m_c.start()] + f_ab + doc[m_c.start():]
# El anexo A empieza a continuación de las referencias, sin salto de página, para ajustar la extensión.
if "SIN_SALTO_A" in __import__("os").environ:
    k_ab = doc.index(f_ab)
    previo = doc[:k_ab]
    m_salto = re.search(re.escape(salto) + r"\s*$", previo)
    assert m_salto
    doc = previo[:m_salto.start()] + previo[m_salto.start() + len(salto):] + doc[k_ab:]
# 3) Los apartados del anexo C pasan a nivel 3 (fuera del índice)
partes = re.findall(r'<w:p(?: [^>]*)?><w:pPr><w:pStyle w:val="Ttulo2"/></w:pPr>(?:(?!</w:p>).)*?<w:t[^>]*>C\.\d [^<]*</w:t>', doc)
assert len(partes) == 4, len(partes)
for p in partes:
    doc = doc.replace(p, p.replace('w:val="Ttulo2"', 'w:val="Ttulo3"', 1), 1)
anclas_c = re.findall(r'<w:bookmarkStart [^>]*w:name="(_Toc\d+)"/>(?:(?!</w:p>).)*?<w:t[^>]*>C\.\d [^<]*</w:t>', doc)
for a in anclas_c:
    doc = re.sub(r'<w:p(?: [^>]*)?><w:pPr><w:pStyle w:val="TDC2"/>(?:(?!</w:p>).)*?w:anchor="' + a + r'"(?:(?!</w:p>).)*?</w:p>', "", doc, count=1)


# El campo del índice se cerraba en la entrada de C.4: se cierra en la última entrada que queda.
if '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p></w:sdtContent>' not in doc:
    k_fin = doc.index("</w:p></w:sdtContent>")
    doc = doc[:k_fin] + '<w:r><w:fldChar w:fldCharType="end"/></w:r>' + doc[k_fin:]


# ---------------------------------------------------------------- Índice
def entrada(texto, ancla, pagina):
    nr = "<w:rPr><w:noProof/><w:webHidden/></w:rPr>"
    return (f'<w:p><w:pPr><w:pStyle w:val="TDC1"/><w:rPr><w:rFonts w:asciiTheme="minorHAnsi" w:eastAsiaTheme="minorEastAsia" '
            f'w:hAnsiTheme="minorHAnsi" w:cstheme="minorBidi"/><w:b w:val="0"/><w:bCs w:val="0"/><w:noProof/><w:kern w:val="2"/>'
            f'<w:lang w:val="en-US" w:eastAsia="en-US"/><w14:ligatures w14:val="standardContextual"/></w:rPr></w:pPr>'
            f'<w:hyperlink w:anchor="{ancla}" w:history="1"><w:r><w:rPr><w:rStyle w:val="Hipervnculo"/><w:noProof/></w:rPr>'
            f'<w:t>{texto}</w:t></w:r><w:r>{nr}<w:tab/></w:r><w:r>{nr}<w:fldChar w:fldCharType="begin"/></w:r>'
            f'<w:r>{nr}<w:instrText xml:space="preserve"> PAGEREF {ancla} \\h </w:instrText></w:r><w:r>{nr}</w:r>'
            f'<w:r>{nr}<w:fldChar w:fldCharType="separate"/></w:r><w:r>{nr}<w:t>{pagina}</w:t></w:r>'
            f'<w:r>{nr}<w:fldChar w:fldCharType="end"/></w:r></w:hyperlink></w:p>')


def antes_de_entrada(doc, texto_entrada, nuevo):
    k = doc.index(f'<w:t>{texto_entrada}</w:t>', doc.index("<w:sdt>"))
    k = inicio_p(doc, k)
    return doc[:k] + nuevo + doc[k:]


doc = antes_de_entrada(doc, "Referencias", entrada(toc_ids[nombres[0]], nombres[0], "0"))
doc = antes_de_entrada(doc, "Anexo C. Material del taller",
                       entrada(toc_ids[nombres[1]], nombres[1], "0") + entrada(toc_ids[nombres[2]], nombres[2], "0"))

# Páginas del índice: se actualizan todas con las medidas de Word
sdt = doc[doc.index("<w:sdt>"):doc.index("</w:sdt>")]
if MEDIDAS:
    def act(m):
        bloque = m.group(0)
        txt = re.search(r"<w:t>([^<]*)</w:t>", bloque).group(1)
        pag = MEDIDAS.get(txt)
        if pag is None:
            return bloque
        return re.sub(r'(w:fldCharType="separate"/></w:r><w:r><w:rPr><w:noProof/><w:webHidden/></w:rPr><w:t>)\d+(</w:t>)',
                      lambda q: q.group(1) + str(pag) + q.group(2), bloque, count=1)
    sdt2 = re.sub(r"<w:hyperlink w:anchor=.*?</w:hyperlink>", act, sdt, flags=re.S)
    doc = doc.replace(sdt, sdt2, 1)

rels_nuevos = rels
contenido["word/document.xml"] = doc.encode("utf8")
with zipfile.ZipFile(SALIDA, "w", zipfile.ZIP_DEFLATED) as z:
    with zipfile.ZipFile(ORIG) as zo:
        orden = zo.namelist()
    for n in orden:
        z.writestr(n, contenido[n])
print("listo", toc_ids)
