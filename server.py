#!/usr/bin/env python3
"""
Simple HTTP Server to run Ramu Munugoti's LinkedIn Web Application locally.
Accessible on desktop, tablet, or smartphone (over local Wi-Fi).
"""

import http.server
import socketserver
import os
import socket

PORT = 8080

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

if __name__ == "__main__":
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)
    
    local_ip = get_local_ip()
    
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print("\n" + "="*60)
        print("  RAMU MUNUGOTI — LINKEDIN AUTHORITY WEB APP")
        print("="*60)
        print(f"\n[+] Local Browser:    http://localhost:{PORT}")
        print(f"[+] Mobile on Wi-Fi:  http://{local_ip}:{PORT}")
        print("\nPress Ctrl+C to stop the server.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Server stopped cleanly.")
