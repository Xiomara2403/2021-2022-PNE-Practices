from functions import functions as f
import termcolor as t
import http
import json


IP = "127.0.0.1"
PORT = 8080
SERVER = "127.0.0.1:8080"
conn = http.client.HTTPConnection(SERVER)

g = "SCARP"
path_list = ["/listSpecies", "/karyotype", "/chromosomeLength", "/geneList", "/geneSeq", "/geneInfo", "/geneCalc"]

for path in path_list:
    t.cprint("* Testing " + path + "...", "green")

    if path == "/listSpecies":
        limit = input("Enter a limit for the list: ")
        params = "?limit=" + limit + "&json=1"

    elif path == "/karyotype":
        specie = input("Enter a specie: ")
        params = "?specie=" + specie + "&json=1"

    elif path == "/chromosomeLength":
        specie = input("Enter a specie: ")
        n_chromosome = input("Enter a chromosome: ")
        params = "?specie=" + specie + "&chromo=" + n_chromosome + "&json=1"

    elif path == "/geneList":
        chromosome = input("Enter a chromosome: ")
        start = input("Select the start point: ")
        end = input("Select the end point: ")
        params = "?chromosome=" + chromosome + "&start=" + start + "&end=" + end + "&json=1"

    elif path == "/geneSeq":
        params = "?gene=" + g + "&json=1"

    elif path == "/geneInfo":
        params = "?gene=" + g + "&json=1"

    elif path == "/geneCalc":
        params = "?gene=" + g + "&json=1"

    response = f.make_server_request(SERVER, path, params)
    print("Content:")
    if type(response) == dict:
        for k,v in response.items():
            if type(v) == list:
                print(f"{k}:")
                for items in v:
                    print(items)
            else:
                print(f"{k}:{v}")
    if type(response) == list:
        for i in response:
            print(i)