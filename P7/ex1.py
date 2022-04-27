# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json

#PORT = 8080 not needed
SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print(f"SERVER: {SERVER}\n")
print(f"URL: {URL}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS) #we do not need to put the server
    # -- Read the response message from the server
    r1 = conn.getresponse()
    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")
    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    # -- Print the received data
    print(f"CONTENT: {data1['ping']}")  # We can check the type of the key putting TYPE before
    if data1["ping"] == 1:  # JSON transform strings into the cprresponding type int or floats
        print("PING OK! The database is running")
    else:
        print("ERROR! The database is not running")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")

