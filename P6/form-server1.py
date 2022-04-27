import http.server
import socketserver
import termcolor
import pathlib

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        print("GET received! Request line:")

        termcolor.cprint("  " + self.requestline, 'green')
        print("  Command: " + self.command)
        print("  Path: " + self.path)
        if self.path == "/":
            contents = pathlib.Path("html/index.html").read_text()
        elif self.path == "/favicon.ico":
            contents = pathlib.Path("html/ping.html").read_text()
        else:
            try:
                filename = self.path[1:].split("/")[1]
                try:
                    contents = pathlib.Path("html/" + filename + ".html").read_text()
                except FileNotFoundError:
                    contents = pathlib.Path("html/error.html").read_text()
            except IndexError:
                contents = pathlib.Path("html/error.html").read_text()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()
        self.wfile.write(contents.encode())

        return


Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()