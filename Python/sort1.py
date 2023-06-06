import random
import timeit
import matplotlib.pyplot as plt
import sys
import csv

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

# Insertion Sort


def insertionSort(Arr):
    for i in range(1, len(Arr)):
        key = Arr[i]
        j = i-1
        while j >= 0 and Arr[j] > key:
            Arr[j+1] = Arr[j]
            j -= 1
        Arr[j+1] = key

# Selection sort


def selectionSort(Arr):
    for i in range(len(Arr)):
        min = i
        for j in range(i+1, len(Arr)):
            if Arr[j] < Arr[min]:
                min = j
        (Arr[i], Arr[min]) = (Arr[min], Arr[i])

# Bubble Sort


def bubbleSort(Arr):
    for i in range(len(Arr)):
        swapped = False
        for j in range(len(Arr)-1-i):
            if Arr[j] > Arr[j+1]:
                swapped = True
                (Arr[j], Arr[j+1]) = (Arr[j+1], Arr[j])
        if not swapped:
            return

# Heap Sort


def heap(Arr, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and Arr[i] < Arr[l]:
        largest = l
    if r < n and Arr[largest] < Arr[r]:
        largest = r
    if largest != i:
        (Arr[i], Arr[largest]) = (Arr[largest], Arr[i])
        heap(Arr, n, largest)


def heapSort(Arr):
    for i in range(len(Arr)//2-1, -1, -1):
        heap(Arr, len(Arr), i)
    for i in range(len(Arr)-1, 0, -1):
        (Arr[i], Arr[0]) = (Arr[0], Arr[i])
        heap(Arr, i, 0)

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


def quickSort(Arr, start, end):
    if start < end:
        pivot = partition(Arr, start, end)
        quickSort(Arr, start, pivot-1)
        quickSort(Arr, pivot+1, end)

# Wykres czasu sortowania list od liczby elementów (algorytmy)


def wykr(f):
    global Arr
    args = ""
    if f.__name__ == "quickSort":
        args = "Arr,0,len(Arr)-1"
    else:
        args = "Arr"
    print(f.__name__+":\n")
    x1, x2, x3, x4, x5 = [], [], [], [], []
    y1, y2, y3, y4, y5 = [], [], [], [], []
    plt.plot()
    for i in range(1000, 10001, 1000):
        Arr = incr(i)
        result = timeit.timeit(stmt=f.__name__+'('+args+')',
                               globals=globals(), number=10)/10
        x1.append(i)
        y1.append(result*1000)
        print(f"Rosnąca {i}: {result*1000} milisekund")
    plt.plot(x1, y1, label="rosnąca", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        Arr = deincr(i)
        result = timeit.timeit(stmt=f.__name__+'('+args+')',
                               globals=globals(), number=10)/10
        x2.append(i)
        y2.append(result*1000)
        print(f"Malejąca {i}: {result*1000} milisekund")
    plt.plot(x2, y2, label="malejąca", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        Arr = ashape(i)
        result = timeit.timeit(stmt=f.__name__+'('+args+')',
                               globals=globals(), number=10)/10
        x3.append(i)
        y3.append(result*1000)
        print(f"A-kształtna {i}: {result*1000} milisekund")
    plt.plot(x3, y3, label="A-kształt", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        Arr = vshape(i)
        result = timeit.timeit(stmt=f.__name__+'('+args+')',
                               globals=globals(), number=10)/10
        x4.append(i)
        y4.append(result*1000)
        print(f"V-kształtna {i}: {result*1000} milisekund")
    plt.plot(x4, y4, label="V-kształt", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        Arr = randomowa(i)
        result = timeit.timeit(stmt=f.__name__+'('+args+')',
                               globals=globals(), number=100)/100
        x5.append(i)
        y5.append(result*1000)
        print(f"Losowa {i}: {result*1000} milisekund")
    plt.plot(x5, y5, label="losowa", alpha=0.7)
    plt.xlabel("Elementy listy")
    plt.ylabel("Czas sortowania")
    plt.title(f'Złożoność obliczeniowa {f.__name__}')
    plt.legend(loc='upper left')
    plt.savefig(f'Wykres1/{f.__name__}.png', bbox_inches='tight')
    print("\nWykres wygenerowany\n\n")
    plt.clf()
    with open(f"Wykres1\\{f.__name__}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Elementy listy", "Rosnąca", "Malejąca",
                        "A-kształtna", "V-kształtna", "Losowa"])
        for i in range(10):
            writer.writerow([(i+1)*100, round(y1[i], 2), round(y2[i], 2),
                            round(y3[i], 2), round(y4[i], 2), round(y5[i], 2)])


wykr(insertionSort)
wykr(selectionSort)
wykr(bubbleSort)
wykr(heapSort)
wykr(mergeSort)
wykr(quickSort)
