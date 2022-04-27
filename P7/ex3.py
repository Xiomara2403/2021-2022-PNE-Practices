import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/ENSG00000207552"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print(f"SERVER: {SERVER}\n")
print(f"URL: {URL}\n")

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMS)
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print(f"Gene: MIR633 \nDescription: {data1['desc']} \nBases: {data1['seq']}")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")