from math import floor
import numpy as np
from validador import val
### pai é o indice / 2 floor
### filho esquerdo é 2 * pai
### filho direito é 2 * pai + 1
### heap maximo é quando o pai é maior que os filhos

def heapify(arr, n, i):
    pai = i
    e = 2 * i
    d = 2 * i + 1

    if e < n and arr[i] < arr[e]:
        pai = e

    if d < n and arr[pai] < arr[d]:
        pai = d

    if pai != i:
        arr[i], arr[pai] = arr[pai], arr[i]
        heapify(arr, n, pai )

array = np.random.randint(0, 10000, 5000)
n = len(array)

while n > 0:
  n -= 1
  for i in range(floor(n/2), -1, -1):
    heapify(array, n, i)
  array[0], array[n] = array[n], array[0]

print(array)
print(val(array))