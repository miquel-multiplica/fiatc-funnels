"""Servidor local para abrir el prototipo por http:// en vez de file://.

    python3 utils/serve.py     →  http://localhost:8080/funnel-salud-quickwins.html

Sirve la raíz del repo, calculada desde la ubicación de este archivo: antes iba a
una ruta absoluta escrita a mano, que se rompía al mover el script o al clonar el
repo en otra máquina.
"""
import functools
import http.server
import socketserver
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PUERTO = 8080

handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(RAIZ))
with socketserver.TCPServer(("", PUERTO), handler) as httpd:
    print(f"Sirviendo {RAIZ} en http://localhost:{PUERTO}")
    httpd.serve_forever()
