from P2.Client0 import Client

print(f"-----| Practice 3, Exercise 7 |------")

IP = "127.0.0.1"
PORT = 8000

c = Client(IP, PORT)
print(c)

print("* Testing PING...")
response = c.talk("PING")
print(response)

print("* Testing GET...")
for i in range(5):
    response = c.talk(f"GET {i}")
    if i == 0:
        get0 = response
    print(f"GET {i}: {response}")

cmd_list = ["INFO", "COMP", "REV"]
for e in cmd_list:
    print(f"* Testing {e}...")
    msg = e + " " + get0
    response = c.talk(msg)
    if e != "INFO":
        print(msg)
    print(response + "\n")

gene_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
print("* Testing GENE...")
for e in gene_list:
    msg = "GENE " + str(e)
    response = c.talk(msg)
    print(f"GENE {e}:\n{response}\n")