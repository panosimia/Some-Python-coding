def factorR(n):
    if n==1:
        return 1
    else:
        y=n*factorR(n-1)
    return y

print(factorR(5))
