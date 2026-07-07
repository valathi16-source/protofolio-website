#!/usr/bin/env python
import http.server
import socketserver
import os

os.chdir(r'c:\Users\valat\OneDrive\Desktop\my web site')

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    print(f"Open http://localhost:{PORT}/MY%20PROTOFILO%20WEB%20SITE.html in your browser")
    httpd.serve_forever()
