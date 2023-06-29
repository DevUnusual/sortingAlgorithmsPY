"""
###Passos:
# 1. Escolha um elemento da lista, chamado de pivô.
# 2. Jogar o pivo no meio do vetor
# 3. 2 auxiliares para vir da esquerda pra direita 
# 4. depois de separados menores de maiores  chamar a funcao de ordenar para cada um dos lados
"""

import numpy as np
from math import floor
from validador import val

def partition(v, i, f):
    e = i
    d = f
    x = v[np.random.randint(i, f)]
    while e <= d:
        print(f'i = {i} f = {f} x = {x} arr = {v[i:f]}')
        while v[e] < x:
            e += 1
        while v[d] > x:
            d -= 1
        if e <= d:
            v[e], v[d] = v[d], v[e]
            e += 1
            d -= 1
    
    if i < d:
        print(f'i = {i} d = {d}')
        partition(v, i, d)
    if f > e:
        print(f'e = {e} f = {f}')
        partition(v, e, f)

v = np.random.randint(0, 100, 50)
partition(v, 0, (len(v)-1))
print(val(v))