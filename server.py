#!/usr/bin/env python3
"""Serve pomodoro PWA on LAN — accessible from phone."""

import http.server
import os
import socket
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(DIR)

MIME = {
    ".html": "text/html; charset=utf-8",
    ".js":   "application/javascript",
    ".json": "application/manifest+json",
    ".svg":  "image/svg+xml",
}


class Handler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        ext = os.path.splitext(path)[1]
        return MIME.get(ext, "text/plain")

    def do_GET(self):
        if self.path == "/":
            self.path = "/pomodoro.html"
        return super().do_GET()

    def log_message(self, fmt, *args):
        print(f"[{self.client_address[0]}] {args[0]}")


def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()


if __name__ == "__main__":
    PORT = 8765
    ip = get_lan_ip()
    print(f"\n  番茄钟 PWA 服务已启动\n")
    print(f"  Mac 浏览器:  http://localhost:{PORT}")
    print(f"  手机浏览器:  http://{ip}:{PORT}")
    print(f"\n  手机打开后用 Safari/Chrome 添加到主屏幕\n")
    print(f"  Ctrl+C 停止服务\n")

    try:
        http.server.HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\n已停止")
