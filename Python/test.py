import random
import timeit
import sys

sys.setrecursionlimit(12000)

total = 0

# Generatory list


def incr(n):
    Arr = [0]*n
    for i in range(n):
        Arr[i] = i
    return Arr


def deincr(n):
    Arr = incr(n)
    return Arr[::-1]


def ashape(n):
    x = int(n/2)
    left = [0]*x
    right = [0]*x
    for i in range(x):
        left[i] = i
    for i in range(x):
        right[i] = i
    right.reverse()
    return left+right


def vshape(n):
    x = int(n/2)
    left = [0]*x
    right = [0]*x
    for i in range(x):
        right[i] = i
    for i in range(x):
        left[i] = i
    left.reverse()
    return left+right


def randomowa(n):
    return random.sample(range(n), n)

# Insertion sort


def insertionSort(Arr):
    for i in range(1, len(Arr)):
        key = Arr[i]
        j = i-1
        while j >= 0 and Arr[j] > key:
            Arr[j+1] = Arr[j]
            j -= 1
        Arr[j+1] = key


def insertionSort2(Arr):
    global total
    for i in range(1, len(Arr)):
        key = Arr[i]
        j = i-1
        while j >= 0 and Arr[j] > key:
            total += 1
            Arr[j+1] = Arr[j]
            total += 1
            j -= 1
        total += 1
        Arr[j+1] = key
        total += 1

# Merge Sort


def mergeSort(Arr):
    if len(Arr) > 1:
        middle = len(Arr)//2
        L = Arr[:middle]
        R = Arr[middle:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                Arr[k] = L[i]
                i += 1
            else:
                Arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            Arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            Arr[k] = R[j]
            j += 1
            k += 1


def mergeSort2(Arr):
    global total
    if len(Arr) > 1:
        middle = len(Arr)//2
        L = Arr[:middle]
        R = Arr[middle:]
        mergeSort2(L)
        mergeSort2(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                Arr[k] = L[i]
                i += 1
            else:
                Arr[k] = R[j]
                j += 1
            total += 1
            k += 1

        while i < len(L):
            Arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            Arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort


def partition(Arr, begin, end):
    pivot = Arr[end]
    i = begin-1
    for j in range(begin, end):
        if Arr[j] <= pivot:
            i += 1
            (Arr[i], Arr[j]) = (Arr[j], Arr[i])
    (Arr[i+1], Arr[end]) = (Arr[end], Arr[i+1])
    return i+1


def partition2(Arr, begin, end):
    global total
    pivot = Arr[end]
    i = begin-1
    for j in range(begin, end):
        if Arr[j] <= pivot:
            i += 1
            (Arr[i], Arr[j]) = (Arr[j], Arr[i])
            total += 1
        total += 1
    (Arr[i+1], Arr[end]) = (Arr[end], Arr[i+1])
    total += 1
    return i+1


def quickSort(Arr, start, end):
    if start < end:
        pivot = partition(Arr, start, end)
        quickSort(Arr, start, pivot-1)
        quickSort(Arr, pivot+1, end)


def quickSort2(Arr, start, end):
    if start < end:
        pivot = partition2(Arr, start, end)
        quickSort2(Arr, start, pivot-1)
        quickSort2(Arr, pivot+1, end)


print("Lista 10000 elementów losowa")
result1 = 0
result2 = 0
result3 = 0
for _ in range(10):
    Arr = randomowa(10000)
    tmp = timeit.timeit(stmt="insertionSort(Arr)", globals=globals(), number=1)
    result1 += tmp
result1 /= 10
print(f"Insertion sort losowa: {round(result1*1000,2)} ms")
for _ in range(10):
    Arr = randomowa(10000)
    tmp = timeit.timeit(stmt="mergeSort(Arr)", globals=globals(), number=1)
    result2 += tmp
result2 /= 10
print(f"Merge sort losowa: {round(result2*1000,2)} ms")
for _ in range(10):
    Arr = randomowa(10000)
    tmp = timeit.timeit(stmt="quickSort(Arr,0,len(Arr)-1)",
                        globals=globals(), number=1)
    result3 += tmp
result3 /= 10
print(f"Quicksort losowa: {round(result3*1000,2)} ms")

for _ in range(10):
    Arr = randomowa(10000)
    insertionSort2(Arr)
print(f"Insertion sort losowa: {total//10} operacji")
total = 0
for _ in range(10):
    Arr = randomowa(10000)
    quickSort2(Arr, 0, len(Arr)-1)
print(f"Quicksort losowa: {total//10} operacji")
