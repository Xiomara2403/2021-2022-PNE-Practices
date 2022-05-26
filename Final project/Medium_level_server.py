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

gene_dict = {"SCARP": "ENSG00000080603",
           "FRAT1" : "ENSG00000165879",
           "ADA": "ENSG00000196839",
           "FXN": "ENSG00000165060",
           "RNU6_269P": "ENSG00000212379",
           "MIR633": "ENSG00000207552",
           "TTTY4C": "ENSG00000226906",
           "RBMY2YP": "ENSG00000227633",
           "FGFR3": "ENSG00000068078",
           "KDR": "ENSG00000128052",
           "ANK2": "ENSG00000145362"
           }
IP = "127.0.0.1"
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

        gene_list = []
        for k, v in gene_dict.items():
            gene_list.append(k)

        if self.path == "/" or self.path == "/favicon.ico":
            contents = f.read_html_file("index.html") \
                    .render(context={"gene_list": gene_list})
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
                    if len(list_species) == 0:
                        contents = pathlib.Path("html/error.html").read_text()
                    else:
                        contents = f.read_html_file("list_species.html")\
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
                n_chromosome = int(arguments["chromo"][0])
                specie = arguments["specie"][0]
                dicts_specie = f.make_ensembl_request("/info/assembly/" + specie, PARAMS)
                dicts_specie = dicts_specie["top_level_region"]
                for d in dicts_specie:
                    if d["name"] == str(n_chromosome):
                        length = d["length"]
                contents = f.read_html_file("length.html")\
                    .render(context={"specie": specie, "n_chromosome": n_chromosome, "length": length})
            except:
                contents = pathlib.Path("html/error.html").read_text()
        elif path.startswith("/gene") == True:
            if path == "/geneList":
                try:
                    chromosome = arguments["chromosome"][0]
                    start = arguments["start"][0]
                    end = arguments["end"][0]
                    region = chromosome + ":" + start + "-" + end
                    dicts_region = f.make_ensembl_request("/phenotype/region/homo_sapiens/" + region, PARAMS)
                    gen_list = []
                    for d in dicts_region:
                        dicts = d["phenotype_associations"][0]
                        if "attributes" in dicts:
                            a = dicts["attributes"]
                            if "associated_gene" in a:
                                gen = a["associated_gene"]
                                gen_list.append(gen)
                    if len(gen_list) == 0:
                        contents = pathlib.Path("html/error.html").read_text()
                    else:
                        contents = f.read_html_file("genelist.html") \
                            .render(context={"chromosome": chromosome, "start": start, "end": end, "gen_list": gen_list})
                except:
                    contents = pathlib.Path("html/error.html").read_text()
            else:
                gene = arguments["gene"][0]
                gene_id = gene_dict[gene]
                dicts_gene = f.make_ensembl_request("/sequence/id/" + gene_id, PARAMS)
                gene_seq = dicts_gene["seq"]
                if path == "/geneSeq":
                    contents = f.read_html_file("geneseq.html") \
                        .render(context={"gene": gene, "gene_seq": gene_seq})
                elif path == "/geneInfo":
                    geneinfo = dicts_gene["desc"].split(":")
                    gene_start = int(geneinfo[3])
                    gene_end = int(geneinfo[4])
                    gene_length = gene_end - gene_start
                    gene_id = dicts_gene["id"]
                    gene_chromosome = geneinfo[1]
                    contents = f.read_html_file("geneinfo.html") \
                        .render(context={"gene": gene, "gene_start": gene_start, "gene_end": gene_end,
                                         "gene_length": gene_length,"gene_id": gene_id, "gene_chromosome": gene_chromosome})
                elif path == "/geneCalc":
                    gene_length = len(gene_seq)
                    s = Seq(gene_seq)
                    d = s.count_bases()
                    p = Seq.percentages(d)
                    gene_percentages = Seq.convert_message(d, p)
                    contents = f.read_html_file("genecalc.html") \
                        .render(context={"gene": gene, "gene_length": gene_length, "gene_percentages": gene_percentages})
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
