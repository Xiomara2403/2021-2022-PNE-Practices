from seq import Seq

str_list = ["ACCTGC", "Hello? Am I a valid sequence?"]
sequence_list = []

for s in str_list:
    if Seq.valid_sequence2(s):
        sequence_list.append(Seq(s))
    else:
        sequence_list.append(Seq("Error"))

for i in range(0, len(sequence_list)):
    print("Sequence", str(i) + ":", sequence_list[i])
# print(Seq.valid_sequence(s1)) This is not valid, because is not static
