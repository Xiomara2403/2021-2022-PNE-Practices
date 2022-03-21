import socket
from P1.Seq1 import Seq
from P2.Client0 import Client
import termcolor

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8000
IP = "127.0.0.1"  # ipconfig en terminal para conectarme a otro servidor -> ip wifi

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("The server is configured!")
while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode().replace("\n", "").strip()
        splitted_comand = msg.split(" ")
        cmd = splitted_comand[0]
        termcolor.cprint(cmd, "green")
        print(f"Message received: {msg}")
        # print(msg == "PING")
        # print(len(msg))
        if cmd == "PING":  # ATTENTION IN WINDOWS THE MSG IS PING\N
            response = "OK!\n"
            termcolor.cprint("ping command", "green")
            print(response)

        elif cmd == "GET":
            genes = ["ACTG", "ATGT", "CGTA", "CCCC", "ATCG"]
            arg = splitted_comand[1]
            print(arg)
            if int(arg) < 5:
                response = genes[int(arg)]
                print(response)
            else:
                response = "Not sequence associated to that number"

        elif cmd == "INFO":
            arg = splitted_comand[1]
            print(arg)
            length = len(arg) + 1
            d = {"A": 0, "C": 0, "G": 0, "T": 0}
            percentages = []
            for b in arg:
                d[b] += 1
            for c in d.values():
                p = c * 100 / length
                percentages.append(p)
            response = f'A: {d["A"]} ({percentages[0]})\nC: {d["C"]} ({percentages[1]})\n' \
                       f'G: {d["G"]} ({percentages[2]})\nT: {d["T"]} ({percentages[3]})\n'
            print(response)

        elif cmd == "COMP":
            arg = splitted_comand[1]
            print(arg)
            s = Seq(arg)
            response = s.complement()
        elif cmd == "REV":
            arg = splitted_comand[1]
            print(arg)
            response = arg[::-1]
        elif cmd == "GENE":
            pass

        else:
            response = "This command is not available in the server\n"
        cs.send(response.encode())
        cs.close()

# echo "xxxxx"| ./nc 127.0.0.1 8000
