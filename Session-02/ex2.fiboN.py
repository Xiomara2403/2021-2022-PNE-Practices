def fib(n):
    n1 = 0
    n2 = 1
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        for i in range(2, n):  # Be careful, if range is (0, N) we will have 13 numbers, not 11
            num = n1 + n2
            n1 = n2
            n2 = num
        return num


print(fib(11))
