"""
1. divide o vetor ao meio recursivamente
2. ordena os dois vetores de baixo pra cima
"""

import numpy as np

def merge(v, i, m, f):
    n1 = m - i
    n2 = f
    L = []
    R = []
    for x in range(i , n1):
        L.append(v[x])
    for y in range(m, n2):
        R.append(v[y])
    L.append(-1)
    R.append(-1)

    x,y = 0,0

    for k in range(i, f):
        if L[x] < R[y] and L[x] != -1:
            v[k] = L[x]
            x += 1
        else:
            v[k] = R[y]
            y += 1


def mergesort(v, i, f):
    if i < f:
        m = int(np.floor((i+f)/2))
        mergesort(v,i,m)
        mergesort(v,m+1,f)
        merge(v,i,m,f)


v = np.random.randint(0, 100, 6)
print(f'antes : {v}')
mergesort(v, 0, (len(v)-1))
print(f'depois: {v}')