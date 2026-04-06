from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = ""
PORT = 8080

class SimpleHandler(BaseHTTPRequestHandler):
    def send_custom_response(self, status_code, body, content_type='text/html'):
        self.send_response(status_code)
        self.send_header('Content-type', f'{content_type}; charset=utf-8')
        self.end_headers()
        self.wfile.write(body.encode('utf-8'))

    def do_GET(self):
        if self.path == '/':
            self.send_custom_response(200, "Hello from Effective Mobile!")
        else:
            self.send_custom_response(404, "<h1>404</h1><p>Page not found</p>")

def run_server():
    web_server = HTTPServer((HOST, PORT), SimpleHandler)
    print(f"Server started at http://{HOST}:{PORT}")
    
    try:
        web_server.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        print("\nStopping server...")
    finally:
        web_server.shutdown()
    
if __name__ == '__main__':
    run_server()
