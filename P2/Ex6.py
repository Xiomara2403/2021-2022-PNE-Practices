from P1.Seq1 import Seq
from Client0 import Client
import termcolor

PRACTICE = 2
EXERCISE = 6


print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


s = Seq()
f = s.valid_filename()
seq = s.read_fasta(f)

IP = "127.0.0.1"
PORT = 8080
c1 = Client(IP, PORT)
print(c1)

PORT2 = 8081
c2 = Client(IP, PORT2)
print(c2)

gene = f.split('/')[2].replace('.txt', '')
d = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: ""}

for k in d:
    d[k] = seq[:10]
    seq = seq[10:]
termcolor.cprint(f"Sending {gene} Gene to the server, in fragments of 10 bases")
for k in d:
    termcolor.cprint(f"Fragment {k}: {d[k]}", "green")

c1.talk(f"Sending {gene} Gene to the server, in fragments of 10 bases")
c2.talk(f"Sending {gene} Gene to the server, in fragments of 10 bases")

for k in d:
    if k % 2 == 0:
        c1.talk(f"Fragment {k}: {d[k]}")
    else:
        c2.talk(f"Fragment {k}: {d[k]}")