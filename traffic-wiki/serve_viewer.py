#!/Users/ran/WorkSpace/SoftWare/miniconda3/envs/research/bin/python3.10
"""Serve the local Traffic Wiki viewer with caching disabled."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        super().end_headers()


if __name__ == "__main__":
    os.chdir(Path(__file__).resolve().parent)
    address = ("127.0.0.1", 8765)
    print("Traffic Wiki: http://127.0.0.1:8765/viewer.html")
    server = ThreadingHTTPServer(address, NoCacheHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
