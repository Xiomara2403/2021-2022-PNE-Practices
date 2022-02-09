import Seq0
list_genes = ["U5", "ADA", "FRAT1", "FXN"]
for l in list_genes:
    print(len(Seq0.seq_read_fasta("../Session-04/" + l + ".txt")))
