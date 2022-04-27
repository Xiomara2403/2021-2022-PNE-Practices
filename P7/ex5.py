from P1.Seq1 import Seq
import http.client
import json


def percentages(d):
    p = {"A": 0, "C": 0, "G": 0, "T": 0}
    total = sum(d.values())
    for k, v in d.items():
        p[k] = v * 100 / total
    return p


def convert_message(d, p):
    message = ""
    for k, v in d.items():
        message += k + ": " + str(v) + " (" + str(round(p[k], 2)) + "%)" + "\n"
    return message


gene_dict =  {"SCARP": "ENSG00000080603",
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

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print(f"SERVER: {SERVER}\n")
print(f"URL: {URL}\n")

conn = http.client.HTTPConnection(SERVER)

try:
    for key, value in gene_dict.items():
        conn.request("GET", ENDPOINT + value + PARAMS)
        r1 = conn.getresponse()
        print(f"Response received!: {r1.status} {r1.reason}\n")
        data1 = r1.read().decode("utf-8")
        data1 = json.loads(data1)
        s = Seq(data1['seq'])
        d = s.count_bases()
        p = percentages(d)
        info = convert_message(d, p)
        print(f"Gene: {key} \nDescription: {data1['desc']} "
              f"\nLength: {s.len()}\n{info}Most frequent base: {s.most_common_base()}")

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")