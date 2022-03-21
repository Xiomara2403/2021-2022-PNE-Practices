from P1.Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

s = Seq()
f = s.valid_filename()
s.read_fasta(f)

IP = "127.0.0.1"
PORT = 8000

c = Client(IP, PORT)
print(c)

gene = f.split('/')[2].replace('.txt', '')
c.talk(f"Sending {gene} to the server...")

print(f"Sending {gene} to the server...")
response = c.talk(str(s))
print(f"Response:\n {response}")