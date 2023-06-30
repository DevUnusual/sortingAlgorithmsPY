<h1 align="center"> Algotimos de ordenação </h1>
<h3 align="center"> InsertionSort, BubbleSort, MergeSort, QuickSort, HeapSort </h3>

![Static Badge](https://img.shields.io/badge/Status-Finalizado-green)
![Static Badge](https://img.shields.io/badge/Code-Python-Blue?logo=Python)

---

<h2>-> BubbleSort</h2>
  -Funcionamento do BubbleSort é duas estruturas de repetição a primeira vai de 0 a ultima posicao, e o segundo
  vai do ultimo ate a posicao atual da primeira estrutura de repetição, verificando se o numero da posição que ele esta é menor que o numero da posição anterior, caso verdade ele troca.
  Fazendo isso ele leva o menor numero do vetor ate a posição que se encontra o primeiro laço e fica na posição pois ele é o menor ate ali.

---

<h2>-> InsertionSort</h2>
  -Funcionamento do insertion sort, faz x (variavel qualquer) receber o valor da posição atual e vai percorrendo o valor procurando por um numero menor que x, caso encontre troca o valor de x com o valor encontrado, e o valor de x vai para a posição em que encontrou o valor menor que ele.
  A cada ciclo da repetição o menor valor vai parar no inicio do vetor.

---

<h2>-> MergeSort</h2>
  -Divisão o problema em certo número de subproblemas que são instâncias menores do mesmo problema.
    Conquista os subproblemas resolvendo-os recursivamente. Entretanto, se os tamanhos dos subproblemas forem
    suficientemente pequenos, basta resolvê-los de modo direto.
    Combinação as soluções dos subproblemas na solução para o problema original.

---

<h2>-> QuickSort</h2>
  -O quicksort, como a ordenação por intercalação, aplica o paradigma de divisão e conquista introduzido na Seção
    2.3.1. Descrevemos a seguir, o processo de três etapas do método de divisão e conquista para ordenar um subarranjo típico A[p .. r].
    Divisão: Particionar (reorganizar) o arranjo A[p .. r] em dois subarranjos (possivelmente vazios) A[p .. q − 1] e A[q + 1 .. r] tais que, cada elemento de A[p .. q − 1] é menor ou igual a A[q] que, por sua vez, é menor ou igual a cada elemento de A[q + 1 .. r]. Calcular o índice q como parte desse procedimento de particionamento.
    Conquista: Ordenar os dois subarranjos A[p .. q −1] e A[q + 1 .. r] por chamadas recursivas a quicksort.
    Combinação: Como os subarranjos já estão ordenados, não é necessário nenhum trabalho para combiná-los: o arranjo A[p .. r] inteiro agora está ordenado.
    (Trecho retirado do livro: Algoritmos, cormen h - Cap: 7)

---

<h2>-> HeapSort </h2>
  -No Heapsort precisa considerar o vetor como sendo uma heap maxima (ou minima vai depender implementação), a heap é uma estrutura em que os nós pai tem que ser maior que o nó filho ou folhas, para verificar a heap começa a verificação a partir da posição n/2 que vai ser o ultimo nó da arvore, apos esse valor são nós folhas, para cada nó verificar se o pai é maior que seus filhos, caso der False, troque o filho com o pai e verifique no nivel do pai se ele é maior que seus filhos caso True retorne para onde foi chamado e em caso de false troca novamente e refaz as verificaçoes, ao final destas chamadas recursivas o maior valor vai se encontrar na primeira posicao do vetor, troque o valor do ultimo com o primeiro, diminua a variavel que guarda o tamanho do vetor em 1 e chame a função de verificar heap a partir da raiz da arvore. fazendo isso ate o vetor ter tamanho 1 vai deixar o vetor final ordenado.

---

# Autores

| [<img src="https://github.com/DevUnusual.png" width=115><br><sub>Carlos meneses</sub>](https://github.com/DevUnusual) |  [<img src="https://github.com/pumba-dev.png" width=115><br><sub>Paulo Eduardo</sub>](https://github.com/pumba-dev) |  [<img src="https://github.com/usernamegran.png" width=115><br><sub>Gabriel Reis</sub>](https://github.com/usernamegran) |
| :---: | :---: | :---: |

