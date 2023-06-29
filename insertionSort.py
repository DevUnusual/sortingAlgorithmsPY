from math import floor

def insertionSort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i - 1
        while j >= 0 and v[j] > x:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x

v = [10, 6, 8, 2, 4, 1]
print(f'antes : {v}')
insertionSort(v)
print(f'depois: {v}')