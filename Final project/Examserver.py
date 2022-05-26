import http.server
import socketserver
import termcolor
import pathlib
import jinja2 as j
from urllib.parse import parse_qs, urlparse
import json
import http.client
from P1.Seq1 import Seq
from functions import functions as f

PARAMS = "?content-type=application/json"
SERVER = "rest.ensembl.org"
PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        print("GET received! Request line:")
        termcolor.cprint("  " + self.requestline, 'green')
        print("  Command: " + self.command)
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print("The old path was", self.path)
        print("The new path is ", path)
        print("arguments", arguments)

        if self.path == "/" or self.path == "/favicon.ico":
            contents = f.read_html_file("index_exam.html") \
                    .render(context = {})
        elif path == "/listSpecies":
            dict_answer = f.make_ensembl_request("/info/species", PARAMS)
            dict_species = dict_answer["species"]
            max_value = len(dict_species)
            try:
                n_species = arguments["limit"][0]
            except KeyError:
                n_species = 0
            list_species = []
            try:
                if int(n_species) <= max_value:
                    for i in range(0, int(n_species)):
                        v = dict_species[i]
                        v = v["display_name"]
                        list_species.append(v)
                    contents = f.read_html_file("list_species.html") \
                        .render(context={"n_species": n_species, "max_value": max_value, "list_species": list_species})
                else:
                    contents = pathlib.Path("html/error.html").read_text()
            except ValueError:
                contents = pathlib.Path("html/error.html").read_text()
        elif path == "/karyotype":
            try:
                specie = arguments["specie"][0]
                dict_karyotype = f.make_ensembl_request("/info/assembly/" + specie, PARAMS)
                karyotype_list = dict_karyotype["karyotype"]
                contents = f.read_html_file("karyotype.html")\
                    .render(context={"specie": specie, "karyotype_list": karyotype_list})
            except:
                contents = pathlib.Path("html/error.html").read_text()
        elif path == "/chromosomeLength":
            try:
                minlength = int(arguments["minlength"][0])
                specie = arguments["specie"][0]
                dicts_specie = f.make_ensembl_request("/info/assembly/" + specie, PARAMS)
                dicts_specie = dicts_specie["top_level_region"]
                chromo_list = []
                for d in dicts_specie:
                    if d["length"] > minlength and d["coord_system"] == "chromosome" and minlength >= 0:
                        c = d["name"]
                        chromo_list.append(c)
                    else:
                        pass
                if len(chromo_list) == 0:
                    contents = pathlib.Path("html/error.html").read_text()
                else:
                    contents = f.read_html_file("length_exam.html")\
                        .render(context={"specie": specie, "minlength": minlength, "chromo_list": chromo_list})
            except:
                contents = pathlib.Path("html/error.html").read_text()
        else:
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