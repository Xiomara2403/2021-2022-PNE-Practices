import json
import http.client

SERVER = "localhost:8080"
PARAMS = "&json=1"

conn = http.client.HTTPConnection(SERVER)
requests = ["/listSpecies?limit=15", "/karyotype?specie=mouse", "/chromosomeLength?specie=mouse&chromo=3",
            "/chromosome?chromosome=9&start=22125500&end=22136000"]
try:
    for m in requests:
        conn.request("GET", m + PARAMS)
        r1 = conn.getresponse()
        data1 = r1.read().decode("utf-8")
        data1 = json.loads(data1)
        for k,v in data1.items():
            print(k + ":",v)
except ConnectionRefusedError:
    print("Error, unable to connect to the server")

