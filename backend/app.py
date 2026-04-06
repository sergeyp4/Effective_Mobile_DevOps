from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            response_code = 200
            response_text = "Hello from Effective Mobile!"
        else:
            response_code = 404
            response_text = "Page not found"
        self.send_response(response_code)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(response_text.encode())

port = 8080
server_address = ('', port)
httpd = HTTPServer(server_address, SimpleHandler)

print(f"Listening port {port}")
httpd.serve_forever()
