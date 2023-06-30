import numpy as np
from validador import val

def insertionSort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i - 1
        while j >= 0 and v[j] > x:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x

if __name__ == '__main__':
  rdarr = np.random.randint(0, 10000, 5000)
  insertionSort(rdarr)
  print(val(rdarr))