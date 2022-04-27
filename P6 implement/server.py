import http.server
import socketserver
import termcolor
import pathlib
import jinja2 as j
from urllib.parse import parse_qs, urlparse

HTML_FOLDER = "./html/"
LIST_SEQUENCES = ["AAAAAAAA", "TTTTTTT", "CCCCC", "GGGGGG", "ATCGATCG"]
LIST_GENES = ["ADA", "FRAT1", "FXN", "RNU5A", "U5"]
def read_html_file(filename):
    contents = pathlib.Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

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
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print("The old path was", self.path)
        print("The new path is ", path)
        print("arguments", arguments)
        if self.path == "/":
            contents = read_html_file("index.html")\
                .render(context =
                            {"n_sequences": len(LIST_SEQUENCES),
                            "genes": LIST_GENES })
        elif path == "/ping":
            contents = read_html_file(path[1:]+".html").render()
        elif path == "/get":
            n_sequence = int(arguments["n_sequence"][0])
            sequence = LIST_SEQUENCES[n_sequence]
            contents = read_html_file(path[1:] + ".html")\
                .render(context = {
                "n_sequence": n_sequence,
                "sequence": sequence
            })
        elif path == "/gene":
            gene_name = arguments["gene_name"][0]
            sequence = pathlib.Path("sequences/" + gene_name + ".txt").read_text()
            contents = read_html_file(path[1:] + ".html")\
                .render(context = {
                "gene_name": gene_name,
                "sequence": sequence
            })
        elif path == "/operation":
            gene_name = arguments["sequence"][0]
            operation = arguments["operation"][0]
            if operation == "rev":
                contents = read_html_file(path[1:] + ".html")\
                .render(context = {
                "operation": operation,
                "result": sequence[::-1]
            })
            elif operation == "info":
                contents = read_html_file(path[1:] + ".html")\
                .render(context = {
                "operation": operation,
                "result": info_op(s)  # /n does not work in html, here we need the <br> and remember that
                    #we need html language like put <p> Sequence. +arg......."<p>
            })
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