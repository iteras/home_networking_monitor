# !/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from sqllite import Sqlite

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):


    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        ds = Sqlite.ds()
        message = ds.get_all()
        # Write content as utf-8 data
        for data in message:
            self.wfile.write(bytes(data, "utf8"))
        return

    # GET
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("UTF-8")
        print("Posted data: %s" % post_data)


def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('192.168.0.100', 8081)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()