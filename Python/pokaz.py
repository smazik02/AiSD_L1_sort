import random
import sys

sys.setrecursionlimit(12000)

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


total = 0
merges = 0

# Insertion Sort


def insertionSort(Arr):
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

# Selection sort


def selectionSort(Arr):
    global total
    for i in range(len(Arr)):
        min = i
        for j in range(i+1, len(Arr)):
            if Arr[j] < Arr[min]:
                min = j
            total += 1
        (Arr[i], Arr[min]) = (Arr[min], Arr[i])
        total += 1

# Bubble Sort


def bubbleSort(Arr):
    global total
    for i in range(len(Arr)):
        swapped = False
        for j in range(len(Arr)-1-i):
            if Arr[j] > Arr[j+1]:
                total += 1
                swapped = True
                (Arr[j], Arr[j+1]) = (Arr[j+1], Arr[j])
                total += 1
            total += 1
        if not swapped:
            return

# Heap Sort


def heap(Arr, n, i):
    global total
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and Arr[i] < Arr[l]:
        largest = l
    total += 1
    if r < n and Arr[largest] < Arr[r]:
        largest = r
    total += 1
    if largest != i:
        (Arr[i], Arr[largest]) = (Arr[largest], Arr[i])
        total += 1
        heap(Arr, n, largest)


def heapSort(Arr):
    global total
    for i in range(len(Arr)//2-1, -1, -1):
        heap(Arr, len(Arr), i)
    for i in range(len(Arr)-1, 0, -1):
        (Arr[i], Arr[0]) = (Arr[0], Arr[i])
        total += 1
        heap(Arr, i, 0)

# Merge Sort


def mergeSort(Arr):
    global total, merges
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

        merges += 1

# Quick Sort


def partition(Arr, begin, end):
    global total
    pivot = Arr[end]
    i = begin-1
    for j in range(begin, end):
        if Arr[j] <= pivot:
            total += 1
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
        print(f"Pivot = {pivot}")
        quickSort(Arr, start, pivot-1)
        quickSort(Arr, pivot+1, end)


def sortuj(f, n):
    global total, merges
    flag = True
    if f.__name__ == "quickSort":
        flag = False
    print(f.__name__)
    Arr = incr(n)
    print(f"Rosnąca\nTablica wejściowa: {Arr}")
    if flag:
        f(Arr)
    else:
        f(Arr, 0, len(Arr)-1)
    print(f"Tablica wyjściowa: {Arr}")
    print(f"Liczba operacji: {total}")
    total = 0
    if f.__name__ == "mergeSort":
        print(f"Liczba scaleń: {merges}")
        merges = 0
    print(" ")
    Arr = deincr(n)
    print(f"Malejąca\nTablica wejściowa: {Arr}")
    if flag:
        f(Arr)
    else:
        f(Arr, 0, len(Arr)-1)
    print(f"Tablica wyjściowa: {Arr}")
    print(f"Liczba operacji: {total}")
    total = 0
    if f.__name__ == "mergeSort":
        print(f"Liczba scaleń: {merges}")
        merges = 0
    print(" ")
    Arr = ashape(n)
    print(f"A-kształtna\nTablica wejściowa: {Arr}")
    if flag:
        f(Arr)
    else:
        f(Arr, 0, len(Arr)-1)
    print(f"Tablica wyjściowa: {Arr}")
    print(f"Liczba operacji: {total}")
    total = 0
    if f.__name__ == "mergeSort":
        print(f"Liczba scaleń: {merges}")
        merges = 0
    print(" ")
    Arr = vshape(n)
    print(f"V-kształtna\nTablica wejściowa: {Arr}")
    if flag:
        f(Arr)
    else:
        f(Arr, 0, len(Arr)-1)
    print(f"Tablica wyjściowa: {Arr}")
    print(f"Liczba operacji: {total}")
    total = 0
    if f.__name__ == "mergeSort":
        print(f"Liczba scaleń: {merges}")
        merges = 0
    print(" ")
    Arr = randomowa(n)
    print(f"Losowa\nTablica wejściowa: {Arr}")
    if flag:
        f(Arr)
    else:
        f(Arr, 0, len(Arr)-1)
    print(f"Tablica wyjściowa: {Arr}")
    print(f"Liczba operacji: {total}")
    total = 0
    if f.__name__ == "mergeSort":
        print(f"Liczba scaleń: {merges}")
        merges = 0


print("Jakim algorytmem chcesz sortować?")
print("1. Insertion sort")
print("2. Selection sort")
print("3. Bubble sort")
print("4. Heap sort")
print("5. Merge sort")
print("6. Quicksort")
choice = int(input())
print("Wpisz liczbę elementów w tablicy:")
n = int(input())
print("\n")
match choice:
    case 1: sortuj(insertionSort, n)
    case 2: sortuj(selectionSort, n)
    case 3: sortuj(bubbleSort, n)
    case 4: sortuj(heapSort, n)
    case 5: sortuj(mergeSort, n)
    case 6: sortuj(quickSort, n)
