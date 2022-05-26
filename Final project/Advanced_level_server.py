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
IP = "127.0.0.1"
PORT = 8080

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
            filename = "index.html"
            contents = {"gene_list": gene_list}
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
                    filename = "list_species.html"
                    contents = {"n_species": n_species, "max_value": max_value, "list_species": list_species}
                else:
                    filename = "error.html"
                    contents = {}
            except ValueError:
                filename = "error.html"
                contents = {}
        elif path == "/karyotype":
            try:
                specie = arguments["specie"][0]
                dict_karyotype = f.make_ensembl_request("/info/assembly/" + specie, PARAMS)
                karyotype_list = dict_karyotype["karyotype"]
                filename = "karyotype.html"
                contents = {"specie": specie, "karyotype_list": karyotype_list}
            except:
                filename = "error.html"
                contents = {}
        elif path == "/chromosomeLength":
            try:
                n_chromosome = int(arguments["chromo"][0])
                specie = arguments["specie"][0]
                dicts_specie = f.make_ensembl_request("/info/assembly/" + specie, PARAMS)
                dicts_specie = dicts_specie["top_level_region"]
                for d in dicts_specie:
                    if d["name"] == str(n_chromosome):
                        length = d["length"]
                filename = "length.html"
                contents = {"specie": specie, "n_chromosome": n_chromosome, "length": length}
            except:
                filename = "error.html"
                contents = {}
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
                    filename = "genelist.html"
                    contents = {"chromosome": chromosome, "start": start, "end": end, "gen_list": gen_list}
                except:
                    filename = "error.html"
                    contents = {}
            else:
                gene = arguments["gene"][0]
                gene_id = gene_dict[gene]
                dicts_gene = f.make_ensembl_request("/sequence/id/" + gene_id, PARAMS)
                gene_seq = dicts_gene["seq"]
                if path == "/geneSeq":
                    filename = "geneseq.html"
                    contents = {"gene": gene, "gene_seq": gene_seq}
                elif path == "/geneInfo":
                    geneinfo = dicts_gene["desc"].split(":")
                    gene_start = int(geneinfo[3])
                    gene_end = int(geneinfo[4])
                    gene_length = gene_end - gene_start
                    gene_id = dicts_gene["id"]
                    gene_chromosome = geneinfo[1]
                    filename = "geneinfo.html"
                    contents = {"gene": gene, "gene_start": gene_start, "gene_end": gene_end,
                            "gene_length": gene_length,"gene_id": gene_id, "gene_chromosome": gene_chromosome}
                elif path == "/geneCalc":
                    gene_length = len(gene_seq)
                    s = Seq(gene_seq)
                    d = s.count_bases()
                    p = Seq.percentages(d)
                    gene_percentages = Seq.convert_message(d, p)
                    filename = "genecalc.html"
                    contents = {"gene": gene, "gene_length": gene_length, "gene_percentages": gene_percentages}
        else:
            filename = "error.html"
            contents = {}

        self.send_response(200)
        if self.path.split("&")[-1] == "json=1":
            contents = json.dumps(contents)
            self.send_header('Content-Type', 'application/json')
        else:
            contents = f.read_html_file(filename) \
                .render(context=contents)
            self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))
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
