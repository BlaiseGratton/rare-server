from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from users import create_user, login_user


class RareRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_POST(self):
        content_len = int(self.headers.get('content-length', 0))
        raw_body = self.rfile.read(content_len)
        post_body = json.loads(raw_body)

        response = None
        
        if self.path == '/login':
            user = login_user(post_body)
            if user:
                response = {
                    'valid': True,
                    'token': user.id
                }
                self._set_headers(200)
            else:
                response = { 'valid': False }
                self._set_headers(404)

        if self.path == '/register':
            try:
                new_user = create_user(post_body)
                response = {
                    'valid': True,
                    'token': new_user.id
                }
            except Exception as e:
                response = {
                    'valid': False,
                    'error': str(e)
                }
            self._set_headers(201)

        self.wfile.write(json.dumps(response).encode())


def main():
    host = ''
    port = 8088
    print(f'listening on port {port}!')
    HTTPServer((host, port), RareRequestHandler).serve_forever()


if __name__ == "__main__":
    main()