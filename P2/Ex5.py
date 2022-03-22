from P1.Seq1 import Seq
from Client0 import Client
import termcolor

PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

s = Seq()
f = s.valid_filename()
seq = s.read_fasta(f)

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

gene = f.split('/')[2].replace('.txt', '')
d = {1: "", 2: "", 3: "", 4: "", 5: ""}
termcolor.cprint(f"Sending {gene} Gene to the server, in fragments of 10 bases", "green")
for k in d:
    d[k] = seq[:10]
    seq = seq[10:]

for k in d:
    termcolor.cprint(f"Fragment {k}: {d[k]}", "green")

c.talk(f"Sending {gene} Gene to the server, in fragments of 10 bases")

for k in d:
    c.talk(f"Fragment {k}: {d[k]}")