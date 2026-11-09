"""API falsa SOLO para validar la compuerta en el runner. No se integra."""
import json
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Manejador(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/salud":
            return self.responder(200, {"estado": "ok"})
        coincidencia = re.fullmatch(r"/productos/(\d+)", self.path)
        if coincidencia and 1 <= int(coincidencia[1]) <= 100:
            i = int(coincidencia[1])
            return self.responder(200, {"id": i, "nombre": f"Producto {i}", "categoria": "hogar", "precio": 129.9, "visitas": 0})
        return self.responder(404, {"error": "producto no encontrado"})

    def responder(self, estado, cuerpo):
        datos = json.dumps(cuerpo).encode()
        self.send_response(estado)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(datos)))
        self.end_headers()
        self.wfile.write(datos)

    def log_message(self, *args):
        pass


ThreadingHTTPServer(("0.0.0.0", 8000), Manejador).serve_forever()
