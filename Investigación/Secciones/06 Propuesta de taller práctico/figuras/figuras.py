"""Figuras 4 y 5 de la sección 6, con el estilo de las Figuras 1 a 3 (Arial, cajas
redondeadas, azul de énfasis). Se dibuja al doble de tamaño y se reduce."""
import math
import sys
from PIL import Image, ImageDraw, ImageFont

SAL = sys.argv[1]
S = 2  # sobremuestreo
NEGRO, GRIS_T, GRIS_L, GRIS_F = (34, 34, 34), (80, 80, 80), (140, 140, 140), (242, 242, 242)
AZUL, AZUL_F = (31, 78, 121), (221, 230, 243)
FLECHA = (51, 51, 51)
F = "C:/Windows/Fonts/"


def fuente(nombre, px):
    return ImageFont.truetype(F + nombre, px * S)


REG, NEG, CUR = "arial.ttf", "arialbd.ttf", "ariali.ttf"


class Lienzo:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.im = Image.new("RGB", (w * S, h * S), "white")
        self.d = ImageDraw.Draw(self.im)

    def s(self, v):
        return int(round(v * S))

    def caja(self, x0, y0, x1, y1, relleno="white", borde=NEGRO, ancho=4, r=26, discontinua=False):
        if discontinua:
            self.d.rounded_rectangle([self.s(x0), self.s(y0), self.s(x1), self.s(y1)], self.s(r), fill=relleno)
            self.borde_discontinuo(x0, y0, x1, y1, borde, ancho, r)
        else:
            self.d.rounded_rectangle([self.s(x0), self.s(y0), self.s(x1), self.s(y1)], self.s(r),
                                     fill=relleno, outline=borde, width=self.s(ancho))

    def borde_discontinuo(self, x0, y0, x1, y1, color, ancho, r, trazo=26, hueco=16):
        # Lados rectos con trazos; esquinas con arcos continuos.
        s = self.s
        for (a, b, c, e) in [(x0 + r, y0, x1 - r, y0), (x0 + r, y1, x1 - r, y1),
                             (x0, y0 + r, x0, y1 - r), (x1, y0 + r, x1, y1 - r)]:
            self.linea_discontinua([(a, b), (c, e)], color, ancho, trazo, hueco)
        for (bx, by, ini) in [(x0, y0, 180), (x1 - 2 * r, y0, 270), (x1 - 2 * r, y1 - 2 * r, 0), (x0, y1 - 2 * r, 90)]:
            self.d.arc([s(bx), s(by), s(bx + 2 * r), s(by + 2 * r)], ini, ini + 90, fill=color, width=s(ancho))

    def texto(self, x, y, t, fuente_, color=NEGRO, ancla="la"):
        self.d.text((self.s(x), self.s(y)), t, font=fuente_, fill=color, anchor=ancla)

    def centrado(self, cx, cy, lineas, fuentes, colores=None, interlineado=1.25):
        """Texto en varias líneas centrado en (cx, cy)."""
        altos = [f.size / S for f in fuentes]
        total = sum(a * interlineado for a in altos) - altos[-1] * (interlineado - 1)
        y = cy - total / 2
        for i, t in enumerate(lineas):
            c = colores[i] if colores else NEGRO
            self.d.text((self.s(cx), self.s(y + altos[i] / 2)), t, font=fuentes[i], fill=c, anchor="mm")
            y += altos[i] * interlineado

    def linea(self, pts, color=FLECHA, ancho=5):
        self.d.line([(self.s(x), self.s(y)) for x, y in pts], fill=color, width=self.s(ancho), joint="curve")

    def linea_discontinua(self, pts, color, ancho, trazo=18, hueco=14, punteada=False):
        if punteada:
            trazo, hueco = ancho, ancho * 2.4
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            largo = math.hypot(x1 - x0, y1 - y0)
            if largo == 0:
                continue
            ux, uy = (x1 - x0) / largo, (y1 - y0) / largo
            pos = 0.0
            while pos < largo:
                fin = min(pos + trazo, largo)
                self.linea([(x0 + ux * pos, y0 + uy * pos), (x0 + ux * fin, y0 + uy * fin)], color, ancho)
                pos += trazo + hueco

    def punta(self, x, y, dx, dy, color=FLECHA, largo=34, ancho=24):
        n = math.hypot(dx, dy)
        ux, uy = dx / n, dy / n
        bx, by = x - ux * largo, y - uy * largo
        px, py = -uy, ux
        self.d.polygon([(self.s(x), self.s(y)), (self.s(bx + px * ancho / 2), self.s(by + py * ancho / 2)),
                        (self.s(bx - px * ancho / 2), self.s(by - py * ancho / 2))], fill=color)

    def flecha(self, pts, color=FLECHA, ancho=5, punteada=False, ambos=False):
        """Poligonal con punta al final (y al inicio si ambos)."""
        (xa, ya), (xb, yb) = pts[-2], pts[-1]
        n = math.hypot(xb - xa, yb - ya)
        ux, uy = (xb - xa) / n, (yb - ya) / n
        corte = list(pts[:-1]) + [(xb - ux * 30, yb - uy * 30)]
        if ambos:
            (xc, yc), (xd, yd) = pts[1], pts[0]
            m = math.hypot(xd - xc, yd - yc)
            vx, vy = (xd - xc) / m, (yd - yc) / m
            corte[0] = (pts[0][0] - vx * 30, pts[0][1] - vy * 30)
        if punteada:
            self.linea_discontinua(corte, color, ancho, punteada=True)
        else:
            self.linea(corte, color, ancho)
        self.punta(xb, yb, ux, uy, color)
        if ambos:
            self.punta(pts[0][0], pts[0][1], vx, vy, color)

    def guardar(self, ruta):
        self.im.resize((self.w, self.h), Image.LANCZOS).save(ruta, optimize=True)


# --------------------------------------------------------------------------
# Figura 4. Arquitectura del entorno
# --------------------------------------------------------------------------
def figura4():
    W, H = 2950, 1600
    L = Lienzo(W, H)
    g, gb, gc = fuente(REG, 52), fuente(NEG, 56), fuente(REG, 44)
    gi = fuente(CUR, 44)

    # Orquestación
    L.caja(300, 30, 2650, 250, GRIS_F, GRIS_L, 4, discontinua=False)
    L.centrado(1475, 105, ["taller.ps1 · taller.sh · GitHub Actions"], [gb])
    L.centrado(1475, 185, ["preparar · funcionales · ejecutar · exportar · detener"], [gc], [GRIS_T])

    # Servicios
    y0, y1 = 470, 920
    L.caja(100, y0, 800, y1, AZUL_F, AZUL, 5)
    L.centrado(450, 695, ["Gatling", "Java 25 · 2 CPU · 2 GB", "decide el veredicto"], [gb, gc, gi], [AZUL, NEGRO, GRIS_T])
    L.caja(1100, y0, 1850, y1)
    L.centrado(1475, 695, ["API", "Flask + Gunicorn", "1 proceso · 8 hilos", "núcleo 2 fijo · 512 MB"],
               [gb, g, gc, gc], [NEGRO, NEGRO, NEGRO, GRIS_T])
    L.caja(2150, y0, 2850, y1)
    L.centrado(2500, 695, ["PostgreSQL 18.6", "pool de 8 conexiones", "núcleo 3 fijo · 512 MB"],
               [gb, gc, gc], [NEGRO, GRIS_T, GRIS_T])

    # Gatling -> API -> PostgreSQL
    L.flecha([(800, 695), (1100, 695)])
    L.centrado(950, 615, ["HTTP"], [g])
    L.flecha([(1850, 695), (2150, 695)])
    L.centrado(2000, 615, ["SQL"], [g])
    L.centrado(2000, 790, ["2 ms de", "latencia"], [gc, gc], [GRIS_T, GRIS_T], 1.1)

    # Orquestación -> servicios (punteadas)
    for x in (450, 1475, 2500):
        L.flecha([(x, 250), (x, y0)], GRIS_L, 4, punteada=True)

    # Observabilidad
    L.caja(100, 1170, 1620, 1560, "white", GRIS_L, 4, discontinua=True)
    L.texto(135, 1190, "Observabilidad", gi, GRIS_T)
    L.caja(150, 1270, 640, 1510)
    L.centrado(395, 1390, ["Grafana", "13.2.5"], [gb, gc], [NEGRO, GRIS_T])
    L.caja(1000, 1270, 1560, 1510)
    L.centrado(1280, 1390, ["Prometheus", "3.15.1"], [gb, gc], [NEGRO, GRIS_T])
    L.flecha([(640, 1390), (1000, 1390)])
    L.centrado(820, 1328, ["consulta"], [gc], [GRIS_T])
    L.flecha([(1280, 1270), (1280, y1)])
    L.centrado(1445, 1095, ["lee /metrics", "cada 5 s"], [gc, gc], [GRIS_T, GRIS_T], 1.1)
    # orquestación -> observabilidad, por el margen izquierdo
    L.flecha([(300, 140), (40, 140), (40, 1365), (100, 1365)], GRIS_L, 4, punteada=True)

    # pytest
    L.caja(2150, 1170, 2850, 1530)
    L.centrado(2500, 1350, ["pytest", "9.2.0", "contrato y concurrencia"], [gb, gc, gc], [NEGRO, GRIS_T, GRIS_T])
    L.flecha([(2500, 1170), (2500, y1)])
    L.flecha([(2150, 1300), (1700, 1300), (1700, y1)])
    L.centrado(1925, 1235, ["pruebas"], [gc], [GRIS_T])

    L.guardar(SAL + "/fig4.png")


# --------------------------------------------------------------------------
# Figura 5. p95 de cada ejecución de validación frente al umbral
# --------------------------------------------------------------------------
def figura5():
    W, H = 2950, 1330
    L = Lienzo(W, H)
    g, gc, gb, gt = fuente(REG, 48), fuente(REG, 44), fuente(NEG, 50), fuente(REG, 42)
    gi = fuente(CUR, 42)
    x0, x1, yt, yb = 330, 2900, 110, 1020   # área de trazado
    lo, hi = 0.001, 100.0

    def Y(v):  # v en segundos
        return yb - (math.log10(v) - math.log10(lo)) / (math.log10(hi) - math.log10(lo)) * (yb - yt)

    # Rejilla y eje vertical
    marcas = [(0.001, "1 ms"), (0.01, "10 ms"), (0.1, "100 ms"), (1, "1 s"), (10, "10 s"), (100, "100 s")]
    for v, t in marcas:
        L.linea([(x0, Y(v)), (x1, Y(v))], (222, 222, 222), 2)
        L.texto(x0 - 25, Y(v), t, g, GRIS_T, "rm")
    for d in range(-3, 2):
        for k in range(2, 10):
            v = k * 10 ** d
            if lo < v < hi:
                L.linea([(x0 - 12, Y(v)), (x0, Y(v))], GRIS_L, 2)
    L.linea([(x0, yt), (x0, yb)], NEGRO, 4)
    L.linea([(x0, yb), (x1, yb)], NEGRO, 4)
    # Límite de espera de Gatling
    L.linea_discontinua([(x0, Y(60)), (x1, Y(60))], GRIS_L, 3, 20, 14)

    campañas = [
        ("validacion-ci-1", "Runner de GitHub Actions", 3.0,
         [0.114, 0.009, 0.009, 0.008], [58.4, 58.6, 58.9], "3 000 ms"),
        ("validacion-ci-2", "Runner de GitHub Actions", 3.0,
         [0.008, 0.010, 0.009], [59.1, 54.1, 55.3], "3 000 ms"),
        ("validacion-local", "Computadora de desarrollo", 1.0,
         [0.010, 0.010, 0.010], [60.0, 60.0, 60.0], "1 000 ms"),
    ]
    ancho = (x1 - x0) / 3
    for i, (nom, ent, umbral, cor, reg, tum) in enumerate(campañas):
        cx = x0 + ancho * (i + 0.5)
        # Umbral
        L.linea([(cx - 340, Y(umbral)), (cx + 340, Y(umbral))], AZUL, 6)
        L.texto(cx - 340, Y(umbral) - 14, "Umbral de " + tum, gt, AZUL, "lb")
        # Corregida: círculos
        for j, v in enumerate(cor):
            px = cx - 230 + (j - (len(cor) - 1) / 2) * 62
            r = 17
            L.d.ellipse([L.s(px - r), L.s(Y(v) - r), L.s(px + r), L.s(Y(v) + r)], fill=AZUL_F, outline=AZUL, width=L.s(5))
        # Regresión: triángulos
        for j, v in enumerate(reg):
            px = cx + 170 + (j - (len(reg) - 1) / 2) * 62
            r = 21
            y = Y(v)
            L.d.polygon([(L.s(px), L.s(y - r)), (L.s(px - r), L.s(y + r * 0.8)), (L.s(px + r), L.s(y + r * 0.8))],
                        fill=(250, 226, 214), outline=(166, 62, 15))
            L.d.line([(L.s(px), L.s(y - r)), (L.s(px - r), L.s(y + r * 0.8)), (L.s(px + r), L.s(y + r * 0.8)),
                      (L.s(px), L.s(y - r))], fill=(166, 62, 15), width=L.s(5), joint="curve")
        # Rótulos de la campaña
        L.texto(cx, yb + 55, nom, gb, NEGRO, "mm")
        L.texto(cx, yb + 112, ent, gt, GRIS_T, "mm")
        if i:
            L.linea([(x0 + ancho * i, yt + 20), (x0 + ancho * i, yb)], (232, 232, 232), 2)
    L.texto(x0 + 20, Y(60) - 14, "Límite de espera de Gatling (60 s)", gi, GRIS_T, "lb")

    # Leyenda
    ly = 1240
    r = 17
    L.d.ellipse([L.s(430 - r), L.s(ly - r), L.s(430 + r), L.s(ly + r)], fill=AZUL_F, outline=AZUL, width=L.s(5))
    L.texto(470, ly, "corregida", g, NEGRO, "lm")
    tx, rr = 780, 21
    L.d.polygon([(L.s(tx), L.s(ly - rr)), (L.s(tx - rr), L.s(ly + rr * 0.8)), (L.s(tx + rr), L.s(ly + rr * 0.8))],
                fill=(250, 226, 214), outline=(166, 62, 15))
    L.d.line([(L.s(tx), L.s(ly - rr)), (L.s(tx - rr), L.s(ly + rr * 0.8)), (L.s(tx + rr), L.s(ly + rr * 0.8)),
              (L.s(tx), L.s(ly - rr))], fill=(166, 62, 15), width=L.s(5), joint="curve")
    L.texto(820, ly, "regresion", g, NEGRO, "lm")
    L.linea([(1130, ly), (1230, ly)], AZUL, 6)
    L.texto(1250, ly, "umbral del perfil de ejecución", g, NEGRO, "lm")

    # Rotar el rótulo del eje: se dibuja aparte y se pega.
    img = L.im
    tmp = Image.new("RGBA", (L.s(900), L.s(70)), (255, 255, 255, 0))
    ImageDraw.Draw(tmp).text((L.s(450), L.s(35)), "p95 de la medición (escala logarítmica)", font=gc, fill=GRIS_T, anchor="mm")
    tmp = tmp.rotate(90, expand=True)
    return L, tmp


def terminar5(L, tmp):
    L.im.paste(tmp, (L.s(30), L.s(110 + (1020 - 110) / 2) - tmp.size[1] // 2), tmp)
    L.guardar(SAL + "/fig5.png")


figura4()
L, tmp = figura5()
terminar5(L, tmp)
