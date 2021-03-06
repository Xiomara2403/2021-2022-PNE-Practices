import Seq0
list_genes = ["U5", "ADA", "FRAT1", "FXN"]
for l in list_genes:
    filename = "../Session-04/" + l + ".txt"
    seq = Seq0.seq_read_fasta(filename)
    bases = ["A", "C", "T", "G"]
    print("Bases in gene:", l)
    for b in bases:
        count = Seq0.seq_count_bases(seq, b)
        print(b + ":", count)