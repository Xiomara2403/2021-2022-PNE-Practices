import jinja2 as j
import json
import http.server
import http.client
import pathlib

class functions:

    def make_ensembl_request(url, PARAMS):
        SERVER = "rest.ensembl.org"
        conn = http.client.HTTPConnection(SERVER)
        try:
            conn.request("GET", url + PARAMS)
            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            data1 = r1.read().decode("utf-8")
            data1 = json.loads(data1)
            return data1
        except ConnectionRefusedError:
            return "ERROR! Cannot connect to the Server"

    def make_server_request(SERVER, url, params):
        conn = http.client.HTTPConnection(SERVER)
        try:
            conn.request("GET", url + params)
            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            data1 = r1.read().decode("utf-8")
            data1 = json.loads(data1)
            return data1
        except ConnectionRefusedError:
            return "ERROR! Cannot connect to the Server"

    def read_html_file(filename):
        HTML_FOLDER = "./html/"
        contents = pathlib.Path(HTML_FOLDER + filename).read_text()
        contents = j.Template(contents)
        return contents