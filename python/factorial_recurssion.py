def factorial(n):
    if(n==1):
        return 1
    nn = n * factorial(n-1)
    print(nn, n)
    return nn
print(factorial(4))