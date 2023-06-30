"""
###Passos:
# 1. Escolha um elemento da lista, chamado de pivô.
# 2. Jogar o pivo no meio do vetor
# 3. 2 auxiliares para vir da esquerda pra direita 
# 4. depois de separados menores de maiores  chamar a funcao de ordenar para cada um dos lados
"""

import numpy as np
from validador import val

def quickSort(v, i, f):
    e = i
    d = f
    x = v[np.random.randint(i, f)]
    while e <= d:
        while v[e] < x:
            e += 1
        while v[d] > x:
            d -= 1
        if e <= d:
            v[e], v[d] = v[d], v[e]
            e += 1
            d -= 1
    
    if i < d:
        quickSort(v, i, d)
    if f > e:
        quickSort(v, e, f)

if __name__ == '__main__':
  rdarr = np.random.randint(0, 10000, 5000)
  quickSort(rdarr, 0, len(rdarr)-1)
  print(val(rdarr))