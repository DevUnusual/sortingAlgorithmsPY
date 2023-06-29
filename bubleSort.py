"""Bubble Sort
Percorre o vetor da ultima posição ate a i
verificando se o elemento de j é menor que o elemento anterior
caso verdade troca os elementos de posição
"""

def bubbleSort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-1, i, -1 ):
            if v[j] < v[j-1]:
                v[j], v[j-1] = v[j-1], v[j]

v = [10, 6, 8, 2, 4, 1]
print(f'antes : {v}')
bubbleSort(v)
print(f'depois: {v}')