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
    if valid_filename:
        seq = open(filename, "r").read()
        seq = seq[seq.find("\n"):].replace("\n", "")
    return seq


def seq_len(filename):
    seq = seq_read_fasta(filename)
    length = len(seq)
    return length


def seq_count_bases(seq, b):
    count = seq.count(b)
    return count


def seq_count(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1
    return d


def seq_reverse(seq):
    new_seq = ""
    for e in seq:
        new_seq = e + new_seq
    return new_seq


def seq_complement(seq):
    complement_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}
    new_seq = ""
    for e in seq:
        for b in complement_dict:
            if e == b:
                new_seq += complement_dict[b]
    return new_seq


def most_common_base(seq):
    count_dict = seq_count(seq)
    most_common = ""
    for b in count_dict:
        if most_common == "":
            most_common = b
        elif int(count_dict[b]) > count_dict[most_common]:
            most_common = b
    return most_common

