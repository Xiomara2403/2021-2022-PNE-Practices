from P2.Client0 import Client

print(f"-----| Practice 3, Exercise 7 |------")

IP = "127.0.0.1"
PORT = 8000

c = Client(IP, PORT)
print(c)

command_list = ["PING", "GET", "INFO", "COMP", "REV", "GENE"]

gene_list = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

for cmd in command_list:
    print("* Testing " + cmd + "...")
    if cmd == "PING":
        response = c.talk(cmd)
        print(response)

    elif cmd == "GET":
        for e in range(5):
            msg = cmd + " " + str(e)
            response = c.talk(msg)
            if e == 0:
                get0 = response

            print(f"{cmd} {e}: {response}", end= "" )
        print()

    elif cmd == "INFO":
        msg = cmd + " " + get0
        response = c.talk(msg)
        print(response)

    elif cmd == "COMP":
        msg = cmd + " " + get0
        print(msg, end= "")
        response = c.talk(msg)
        print(response)

    elif cmd == "REV":
        msg = cmd + " " + get0
        print(msg, end= "")
        response = c.talk(msg)
        print(response)

    elif cmd == "GENE":
        for e in gene_list:
            msg = cmd + " " + str(e)
            response = c.talk(msg)
            print(f"{cmd} {e}:\n{response}\n[...]\n{response[-10:]}\n")