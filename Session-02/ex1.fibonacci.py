N = 11  # Constant variable
n1 = 0
n2 = 1
print(n1,end=" ")
print(n2, end=" ")
for i in range(2, N):  # Be careful, if range is (0, N) we will have 13 numbers, not 11
    num = n1 + n2
    print(num, end=" ")
    n1 = n2
    n2 = num

