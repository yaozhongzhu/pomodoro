#!/usr/bin/env python3
"""番茄钟 — 启动服务端，浏览器 + 手机均可访问"""

import subprocess
import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    server = os.path.join(DIR, "server.py")
    if not os.path.exists(server):
        print("错误：找不到 server.py")
        sys.exit(1)
    subprocess.run([sys.executable, server])
