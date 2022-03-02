from Seq1 import Seq
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {Seq.len(s1)}) {s1} \n {s1.count_bases()}")
print(f"Sequence 1: (Length: {Seq.len(s2)}) {s2} \n {s2.count_bases()}")
print(f"Sequence 1: (Length: {Seq.len(s3)}) {s3} \n {s3.count_bases()}")