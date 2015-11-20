from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import Client
import cgi
class HttpProcessor(BaseHTTPRequestHandler):

    def do_POST(self):

        if 'application/json' == self.headers.get('content-type'):

            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
                     })

            print(form)

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            json = Client.get_Json()
            self.wfile.write(json)

        else :
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            self.wfile.write("This HTML response")

    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        self.wfile.write("This HTML response")

serv = HTTPServer(("localhost",80),HttpProcessor)
serv.serve_forever()