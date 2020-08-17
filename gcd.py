def gcd(m,n):
    op = []
    for i in range(1,m+1):
        if m % i == 0:
            op.append(i)
    jp = []
    for i in range(1,n+1):
        if n % i == 0:
            jp.append(i)

    k = []
    for i in op:
        if i in jp:
            k.append(i)
    return k

result = gcd(25,65)
print(result)
