import Seq0
filename = Seq0.valid_filename()  # U5.txt
seq = Seq0.seq_read_fasta(filename)
print(seq[:20])