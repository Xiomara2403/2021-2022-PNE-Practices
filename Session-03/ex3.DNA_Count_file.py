def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1
    return d


with open("ex3.DNA.txt", "r") as f:
    sequences = f.readlines()
    for seq in sequences:
        new_seq = seq.replace("\n", "")
        print("Total length:", len(new_seq))
        for k, v in count_bases(new_seq).items():  # IMPORTANT, is better than print each key and value
            print(k + ":", v)
