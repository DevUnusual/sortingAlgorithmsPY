"""Bubble Sort
Percorre o vetor da ultima posição ate a i
verificando se o elemento de j é menor que o elemento anterior
caso verdade troca os elementos de posição
"""

import numpy as np
from validador import val

def bubbleSort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-1, i, -1 ):
            if v[j] < v[j-1]:
                v[j], v[j-1] = v[j-1], v[j]

if __name__ == '__main__':
  rdarr = np.random.randint(0, 10000, 5000)
  bubbleSort(rdarr)
  print(val(rdarr))
