def binomial(n,k):
    if k<0:
        print("Error")
        return -1
    else:
        t=1.0
        for i in range(k):
            t = t*(n-i)/(k-i)
        return t

print(binomial(10,2))
