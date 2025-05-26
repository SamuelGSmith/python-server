from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 9999

class BespokeHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Bespoke GET Response</title></head>", "utf-8"))

server = HTTPServer(('localhost', PORT), BespokeHTTP)

print('Starting Bespoke HTTP Server on port {}'.format(PORT))
server.serve_forever()
server.server_close()
