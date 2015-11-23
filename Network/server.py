from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import JsonCreator as creator
class HttpProcessor(BaseHTTPRequestHandler):

    def do_POST(self):

        if 'application/json' == self.headers.get('content-type'):

            length = int(self.headers.getheader('content-length'))
            data = self.rfile.read(length)
            dict = creator.parse(data)

            if (True == dict['all']):

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()

                jsn = creator.resp_all_events_json()
                self.wfile.write(jsn)

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