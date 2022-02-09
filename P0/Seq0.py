def seq_ping():
    print("OK")


def valid_filename():
    exit = False
    while not exit:
        try:
            FOLDER = "../Session-04/"
            FILENAME = input("What do you want to open?: ")
            filename = FOLDER + FILENAME
            exit = True
            return filename
        except FileNotFoundError:
            print("no")


def seq_read_fasta(filename):
    seq = open(filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_count(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1
    return d


