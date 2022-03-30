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

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)

        # Print the resource requested (the path)
        print("  Path: " + self.path)
        if self.path == "/":
            # This new contents are written in HTML language
            # f = open("html/index.html", "r").read() or
            contents = pathlib.Path("html/index.html").read_text()
        elif self.path == "/favicon.ico":
            contents = pathlib.Path("html/index.html").read_text()
        else:
            try:
                filename = self.path[1:].split("/")[1]
                try:
                    contents = pathlib.Path("html/" + filename + ".html").read_text()
                except FileNotFoundError:
                    contents = pathlib.Path("html/error.html").read_text()
            except IndexError:
                contents = pathlib.Path("html/error.html").read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()