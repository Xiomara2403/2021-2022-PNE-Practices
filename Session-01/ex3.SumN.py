# Function for calculating the sum of the
# N first integer numbers

def sumn(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

# -- The main program starts here
print("Sum of the 20 first integers: ", sumn(20))
print("Sum of the 100, first integers: ", sumn(100))

# In order to see it step by step inside the function, we press "Step into"
# And now we will be able to see the variables and values
# If the function inside is correct, then we press "Step out" and we continuous outside the function
