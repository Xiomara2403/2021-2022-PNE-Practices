from Seq1 import Seq
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

bases = ["A", "C", "T", "G"]

print(f"Sequence 1: (Length: {Seq.len(s1)}) {s1}")
for b in bases:
    count = s1.count_b(b)
    print(b + ":", count)
print(f"Sequence 2: (Length: {Seq.len(s2)}) {s2}")
for b in bases:
    count = s2.count_b(b)
    print(b + ":", count)
print(f"Sequence 3: (Length: {Seq.len(s3)}) {s3}")
for b in bases:
    count = s3.count_b(b)
    print(b + ":", count)