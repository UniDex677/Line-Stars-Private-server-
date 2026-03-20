import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Server is running')

def start_http_server():
    port = int(os.environ.get("PORT", 8080))
    httpd = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    httpd.serve_forever()

# Запускаем HTTP-сервер в отдельном потоке
http_thread = threading.Thread(target=start_http_server, daemon=True)
http_thread.start()

# Ваш существующий код
from Classes.ServerConnection import ServerConnection
port = int(os.environ.get("PORT", 9339))
ServerConnection(("0.0.0.0", 10000))
