from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class HttpProcessor(BaseHTTPRequestHandler):


    def do_POST(self):




        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()





        self.wfile.write("hello !")

    def do_GET(self):

        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write("hello !")
        self.wfile.write("ggg")


serv = HTTPServer(("localhost",80),HttpProcessor)
serv.serve_forever()

print(serv)
