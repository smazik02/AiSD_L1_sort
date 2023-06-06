import random
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
    global total
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
        quickSort(Arr, start, pivot-1)
        quickSort(Arr, pivot+1, end)

# Wykres liczby operacji k (porównań i zamian) od liczby elementów (algorytmy)


def wykr(f):
    global total
    func = ""
    flag = True
    match f.__name__:
        case "insertionSort":
            func = "Insertion sort"
        case "selectionSort":
            func = "Selection sort"
        case "bubbleSort":
            func = "Bubble sort"
        case "heapSort":
            func = "Heap sort"
        case "mergeSort":
            func = "Merge sort"
        case "quickSort":
            func = "Quick sort"
            flag = False
        case _:
            print("Nie ma takiej funkcji")
            return

    print(func+":\n")
    x1, x2, x3, x4, x5 = [], [], [], [], []
    y1, y2, y3, y4, y5 = [], [], [], [], []
    plt.plot()
    for i in range(1000, 10001, 1000):
        Arr = incr(i)
        total = 0
        if flag:
            f(Arr)
        else:
            f(Arr, 0, len(Arr)-1)
        x1.append(i)
        y1.append(total)
        print(f"Rosnąca {i}: {total} operacji")
    plt.plot(x1, y1, label="rosnąca", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        Arr = deincr(i)
        total = 0
        if flag:
            f(Arr)
        else:
            f(Arr, 0, len(Arr)-1)
        x2.append(i)
        y2.append(total)
        print(f"Malejąca {i}: {total} operacji")
    plt.plot(x2, y2, label="malejąca", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        Arr = ashape(i)
        total = 0
        if flag:
            f(Arr)
        else:
            f(Arr, 0, len(Arr)-1)
        x3.append(i)
        y3.append(total)
        print(f"A-kształtna {i}: {total} operacji")
    plt.plot(x3, y3, label="A-kształt", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        Arr = vshape(i)
        total = 0
        if flag:
            f(Arr)
        else:
            f(Arr, 0, len(Arr)-1)
        x4.append(i)
        y4.append(total)
        print(f"V-kształtna {i}: {total} operacji")
    plt.plot(x4, y4, label="V-kształt", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        Arr = randomowa(i)
        total = 0
        for _ in range(10):
            if flag:
                f(Arr)
            else:
                f(Arr, 0, len(Arr)-1)
        x5.append(i)
        y5.append(total//10)
        print(f"Losowa {i}: {total//10} operacji")
    plt.plot(x5, y5, label="losowa", alpha=0.7)
    plt.xlabel("Elementy listy")
    plt.ylabel("Liczba operacji")
    plt.title(f'Złożoność obliczeniowa {f.__name__}')
    plt.legend(loc='upper left')
    plt.savefig(f'Wykres4/{f.__name__}.png', bbox_inches='tight')
    print("\nWykres wygenerowany\n\n")
    plt.clf()
    with open(f"Wykres4\\{f.__name__}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Elementy listy", "Rosnąca", "Malejąca",
                        "A-kształtna", "V-kształtna", "Losowa"])
        for i in range(10):
            writer.writerow([(i+1)*1000, y1[i], y2[i], y3[i], y4[i], y5[i]])


wykr(insertionSort)
wykr(selectionSort)
wykr(bubbleSort)
wykr(heapSort)
wykr(mergeSort)
wykr(quickSort)
