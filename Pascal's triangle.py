def pascal(n):
    if n==1:
        return [1]
    else:
        line=[1]
        p_line=pascal(n-1)
        l=len(p_line)
        for i in range(l-1):
            line.append(p_line[i]+p_line[i+1])
        line.append(1)
    return line

print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))
print(pascal(5))
