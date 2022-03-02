from Seq1 import Seq
s = Seq()
filename = s.valid_filename()
s.read_fasta(filename)

print(f"Sequence 1: (Length: {Seq.len(s)}) {s} \n {s.count_bases()}")
print("Rev:", s.reverse())
print("Comp:", s.complement())