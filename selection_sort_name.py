def lastname_first(name1,name2):
    return name1.split()[1]<name2.split()[1]

def find_min(L,b):
    smallest=b
    i=b+1
    while i!=len(L):
        if lastname_first(L[i],L[smallest]):
            smallest=i
        i+=1
    return smallest

def selection_sort(L):
    i=0
    while i!=len(L):
        smallest=find_min(L,i)
        l[i],L[smallest]=L[smallest],L[i]
        i+=1
    return L

c=["John Lennon","John Kennedy"]
l=["Albert Einstein","Mata Hari"]
print(selection_sort(c))
print(selection_sort(l))
