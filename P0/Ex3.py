import Seq0
list_genes = ["U5", "ADA", "FRAT1", "FXN"]
for l in list_genes:
    filename = "../Session-04/" + l + ".txt"
    length = Seq0.seq_len(filename)
    print("Length of", l + ":", length)
