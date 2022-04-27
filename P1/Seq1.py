class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if not self.valid_sequence():
            if self.strbases == "NULL":
                print("NULL seq created")
            else:
                self.strbases = "ERROR"
                print("INVALID seq!")
        else:
            print("New sequence created!")

    @staticmethod  # Check if the sequence is valid outside the class
    def valid_sequence2(sequence):
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "T" and c != "G":
                valid = False
            i += 1
        return valid

    def valid_sequence(self):  # Dynamic method
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "T" and c != "G":
                valid = False
            i += 1
        return valid

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return "0"
        else:
            return len(self.strbases)

    def count_b(self, b):
        count = 0
        if self.strbases != "NULL" and self.strbases != "ERROR":
            for e in self.strbases:
                if e == b:
                    count += 1
        return count

    def count_bases(self):
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        if self.strbases != "NULL" and self.strbases != "ERROR":
            for b in self.strbases:
                d[b] += 1
        return d

    def reverse(self):
        new_seq = ""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            for e in self.strbases:
                new_seq = e + new_seq
            return new_seq

    def complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            complement_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}
            new_seq = ""
            for e in self.strbases:
                for b in complement_dict:
                    if e == b:
                        new_seq += complement_dict[b]
            return new_seq

    def valid_filename(self):
        exit = False
        while not exit:
            try:
                FOLDER = "../Session-04/"
                FILENAME = input("What do you want to open?: ")
                filename = FOLDER + FILENAME + ".txt"
                exit = True
                return filename
            except FileNotFoundError:
                print("no")

    def read_fasta(self, filename):
        try:
            f = open(filename, "r").read()
            self.strbases = f[f.find("\n"):].replace("\n", "")
            if self.valid_sequence():
                seq = self.strbases
                return seq
            else:
                return "It is not a valid sequence"
        except FileNotFoundError:
            return "Gene not found"

    def most_common_base(self):
        count_dict = self.count_bases()
        most_common = ""
        for b in count_dict:
            if most_common == "":
                most_common = b
            elif int(count_dict[b]) > count_dict[most_common]:
                most_common = b
        return most_common

    def percentages(d):
        p = {"A": 0, "C": 0, "G": 0, "T": 0}
        total = sum(d.values())
        for k, v in d.items():
            p[k] = v * 100 / total
        return p

    def convert_message(d, p):
        message = ""
        for k, v in d.items():
            message += k + ": " + str(v) + " (" + str(round(p[k], 2)) + "%)" + "\n"
        return message
