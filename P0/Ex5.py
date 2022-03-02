import Seq0
list_genes = ["U5", "ADA", "FRAT1", "FXN"]
for l in list_genes:
    filename = "../Session-04/" + l + ".txt"
    seq = Seq0.seq_read_fasta(filename)
    print("Bases in gene:", l)
    d = Seq0.seq_count(seq)
    print (d)