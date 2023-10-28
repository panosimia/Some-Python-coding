def sumsq(n):
    if n <=0:
        return 0
    s=0
    for i in range(1,n+1):
        s+= i*i
    return s

n=input ("Give the number: ")
n=int(n)
print("The sum of the sqares of the first",n," integers is", sumsq(n))
