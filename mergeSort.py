"""
1. divide o vetor ao meio recursivamente
2. ordena os dois vetores de baixo pra cima
"""

import numpy as np
from math import floor

def merge(v, i, m, f):
    if i == f:
        return
    L = []
    R = []
    x,y = i,m+1
    while x <= m:
        L.append(v[x])
        x += 1
    while y <= f:
        R.append(v[y])
        y += 1

    L.append(-1)
    R.append(-1)

    x,y,k = 0,0,i

    while (L[x] != -1 or R[y] != -1):
        if (L[x] < R[y] or R[y] == -1) and L[x] != -1:
            v[k] = L[x]
            x += 1
            k += 1
        else:
            v[k] = R[y]
            y += 1
            k += 1


def mergesort(v, i, f):
    if i < f:
        m = floor((i+f)/2)
        mergesort(v,i,m)
        mergesort(v,m+1,f)
        merge(v,i,m,f)


v = [10, 6, 8, 2, 4, 1]
print(f'antes : {v}')
mergesort(v, 0, (len(v)-1))
print(f'depois: {v}')