from math import floor
import numpy as np
from validador import val
### pai é o indice / 2 floor
### filho esquerdo é 2 * pai
### filho direito é 2 * pai + 1
### heap maximo é quando o pai é maior que os filhos

def heapify(arr, n, i):
    maior = i
    e = 2 * i
    d = 2 * i + 1

    if e <= n and arr[maior] < arr[e]:
        maior = e

    if d <= n and arr[maior] < arr[d]:
        maior = d

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior )


def heapSort(array):
  n = len(array)
  init = floor(n/2)
  while n > 0:
    for i in range(init, -1, -1):
      heapify(array, n-1, i)
    array[0], array[n-1] = array[n-1], array[0]
    n -= 1


if __name__ == '__main__':
  rdarr = np.random.randint(0, 10000, 5000)
  heapSort(rdarr)
