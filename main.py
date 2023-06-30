### Importacao dos algoritmos de Ordenacao
from sortAlgorithms.bubleSort import bubbleSort
from sortAlgorithms.insertionSort import insertionSort
from sortAlgorithms.mergeSort import mergeSort
from sortAlgorithms.quickSort import quickSort
from sortAlgorithms.heapSort import heapSort

### biblioteca para gerar os vetores de testes
import numpy as np

### biblioteca para medir o tempo de execucao
import time

if __name__ == "__main__":
    TAMANHO = 500
    aleatorio = np.random.randint(0, 10000, TAMANHO)
    crescente = np.arange(0, TAMANHO)
    decrescente = np.arange(TAMANHO, 0, -1)
    
    pos = 1
    while pos != 16:
      start = time.time()
      match pos:
          case 1:
              bubbleSort(aleatorio.copy())
          case 2:
              bubbleSort(crescente.copy())
          case 3:
              bubbleSort(decrescente.copy())
          case 4:
              insertionSort(aleatorio.copy())
          case 5:
              insertionSort(crescente.copy())
          case 6:
              insertionSort(decrescente.copy())
          case 7:
              mergeSort(aleatorio.copy(), 0, len(aleatorio.copy())-1)
          case 8:
              mergeSort(crescente.copy(), 0, len(crescente.copy())-1)
          case 9:
              mergeSort(decrescente.copy(), 0, len(decrescente.copy())-1)
          case 10:
              quickSort(aleatorio.copy(), 0, len(aleatorio.copy())-1)
          case 11:
              quickSort(crescente.copy(), 0, len(crescente.copy())-1)
          case 12:
              quickSort(decrescente.copy(), 0, len(decrescente.copy())-1)
          case 13:
              heapSort(aleatorio.copy())
          case 14:
              heapSort(crescente.copy())
          case 15:
              heapSort(decrescente.copy())
      end = time.time()
      pos += 1
      total = end - start

      match pos - 1:
          case 1:
              print(f"Bubble Sort Aleatorio:      {total : {2}.{5}}ms")
          case 2:
              print(f"Bubble Sort crescente:      {total : {2}.{5}}ms")
          case 3:
              print(f"Bubble Sort decrescente:    {total : {2}.{5}}ms\n")
          case 4:
              print(f"Insertion Sort Aleatorio:   {total : {2}.{5}}ms")
          case 5:
              print(f"Insertion Sort crescente:   {total : {2}.{5}}ms")
          case 6:
              print(f"Insertion Sort decrescente: {total : {2}.{5}}ms\n")
          case 7:
              print(f"Merge Sort Aleatorio:       {total : {2}.{5}}ms")
          case 8:
              print(f"Merge Sort crescente:       {total : {2}.{5}}ms")
          case 9:
              print(f"Merge Sort decrescente:     {total : {2}.{5}}ms\n")
          case 10:
              print(f"quick Sort Aleatorio:       {total : {2}.{5}}ms")
          case 11:
              print(f"quick Sort crescente:       {total : {2}.{5}}ms")
          case 12:
              print(f"quick Sort decrescente:     {total : {2}.{5}}ms\n")
          case 13:
              print(f"heap Sort Aleatorio:        {total : {2}.{5}}ms")
          case 14:
              print(f"heap Sort crescente:        {total : {2}.{5}}ms")
          case 15:
              print(f"heap Sort decrescente:      {total : {2}.{5}}ms")
