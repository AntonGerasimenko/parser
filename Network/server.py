from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import JsonCreator as creator

host = "192.168.5.55"
class HttpProcessor(BaseHTTPRequestHandler):

    def do_POST(self):

        if 'application/json' == self.headers.get('content-type'):

            print "Content-type: application/json"

            length = int(self.headers.getheader('content-length'))
            print "Data lenght " + str(length)
            data = self.rfile.read(length)
            print "Read data : " + data
            ids = set()
            time = 0
            all = False

            for item in creator.parse(data):
                print item.keys()
                for key in item.keys():
                    if key == 'all':
                        print "Return All events..."
                        all = True
                    elif key == 'id':
                        id = item['id']
                        ids.add(id)
                        print "Add excepion list id = " + str(id)
                    if key == 'time':
                        time = item['time']
                        print "Limited time : " + str(time)
            if all or len(ids) > 0:
                jsn = creator.resp_all_events_json(ids, time)
                self.make_json(jsn)
            else:
                self.make_html()
        else:
            self.make_html()
            return

    def do_GET(self):

         self.send_response(200)
         self.send_header('Content-Type', 'text/html')
         self.end_headers()

         self.wfile.write("This HTML response")

    def make_json(self,jsn):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(jsn)

    def make_html(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        self.wfile.write("This HTML response")

serv = HTTPServer((host,80),HttpProcessor)
serv.serve_forever()