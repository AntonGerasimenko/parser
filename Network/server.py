from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import JsonCreator as creator

host = "192.168.5.55"
class HttpProcessor(BaseHTTPRequestHandler):

    def do_POST(self):

        if 'application/json' == self.headers.get('content-type'):

            print "application/json"

            length = int(self.headers.getheader('content-length'))
            print length
            data = self.rfile.read(length)

            print data

            for item in creator.parse(data):

                break

            if (True == dict['all']):

                print "True"

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()

                jsn = creator.resp_all_events_json()
                self.wfile.write(jsn)

        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            self.wfile.write("This HTML response")

    def do_GET(self):

         self.send_response(200)
         self.send_header('Content-Type', 'text/html')
         self.end_headers()

         self.wfile.write("This HTML response")

serv = HTTPServer((host,80),HttpProcessor)
serv.serve_forever()