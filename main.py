def factOrSum(x,o):
    total = 1
    sumtotal = x
    if o == "factorial":
        for i in range (1,x+1):
            total *= i
        return total
    else:
        for i in range (0, x):
            sumtotal += i
        return sumtotal



print (factOrSum(3, "sum"))