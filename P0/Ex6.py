import Seq0
filename = Seq0.valid_filename()
seq = Seq0.seq_read_fasta(filename)
reverse_seq = Seq0.seq_reverse(seq[:20])
print("Frag:", seq[:20],
      "\nReverse seq:", reverse_seq)