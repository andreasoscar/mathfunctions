def sum(n,i):
    s = 0
    for j in range(1,n+1):
        s += 5/(i+2*j-1)
    return s
for k in range(6,16):
    m = []
    for i in range(1,k+1):
        m.append(sum(k,i))
    print(max(m))
