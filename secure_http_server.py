from http.server import SimpleHTTPRequestHandler, HTTPServer

class SecureHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add security headers
        self.send_header('Strict-Transport-Security', 'max-age=31536000; includeSubDomains')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-XSS-Protection', '1; mode=block')
        self.send_header('Content-Security-Policy', "default-src 'self'")
        super().end_headers()

def run(server_class=HTTPServer, handler_class=SecureHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting secure server on port {port}...')
    httpd.serve_forever()

# Example usage
if __name__ == '__main__':
    run()
