def selection_sort(L):
    i=0
    while i!=len(L):
        smallest=find_min(L,i)
        L[i],L[smallest]=L[smallest],L[i]
        i+=1
    return L

def find_min(L,b):
    smallest=b
    i=b+1
    while i!=len(L):
        if L[i]<L[smallest]:
            smallest=i
        i+=1
    return smallest

c=[19,3,2,41,20,17,15,1,0,36,22]
print (c)
print(selection_sort(c))
