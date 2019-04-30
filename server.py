import http.server
import socketserver

PORT = input("Port (leave blank for default):")
if not PORT:
    PORT = 8080
else:
    PORT = int(PORT)
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Python 3 Webserver running on port", PORT)
    httpd.serve_forever()