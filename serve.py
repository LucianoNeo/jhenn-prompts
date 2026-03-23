#!/usr/bin/env python3
# Simple HTTP server for prompts-site
# Serves on 0.0.0.0:8080 (accessible on local network)

import http.server
import socketserver
import os
import socket

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def get_local_ip():
    """Get the local IP address for network access"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        local_ip = get_local_ip()
        print(f"🎬 Jhenn's VEO3 Prompts Server")
        print(f"=" * 40)
        print(f"Local:   http://localhost:{PORT}")
        print(f"Network: http://{local_ip}:{PORT}")
        print(f"Serving from: {DIRECTORY}")
        print(f"=" * 40)
        print("Press Ctrl+C to stop")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")
