import Seq0
filename = Seq0.valid_filename()
seq = Seq0.seq_read_fasta(filename)
print("The first 20 bases are:\n" + seq[:20])
