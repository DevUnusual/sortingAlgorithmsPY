"""
1. divide o vetor ao meio recursivamente
2. ordena os dois vetores de baixo pra cima
"""

import numpy as np

def mergesort(v, i, f):
    if i < f:
        m = np.floor((i+f)/2)
        mergesort(v,i,m)
        mergesort(v,m+1,f)
        merge(v,i,m,f)


v = np.random.randint(0, 100, 50)
mergeSort(v, 0, len(v)-1)
print(v)