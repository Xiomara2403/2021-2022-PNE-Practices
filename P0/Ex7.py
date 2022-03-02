import Seq0
filename = Seq0.valid_filename()
seq = Seq0.seq_read_fasta(filename)
complement_seq = Seq0.seq_complement(seq[:20])
print("Frag:", seq[:20],
      "\nComplement seq:", complement_seq)