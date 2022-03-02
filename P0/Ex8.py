import Seq0
list_genes = ["U5", "ADA", "FRAT1", "FXN"]
for l in list_genes:
    filename = "../Session-04/" + l + ".txt"
    seq = Seq0.seq_read_fasta(filename)
    most_common = Seq0.most_common_base(seq)
    print("Most common base in gene", l + ":", most_common)