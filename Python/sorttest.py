import random
import timeit
import matplotlib.pyplot as plt
import sys
import csv
import os
from timeit import default_timer as timer

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

# Selection sort


def selectionSort(Arr):
    for i in range(len(Arr)):
        min = i
        for j in range(i+1, len(Arr)):
            if Arr[j] < Arr[min]:
                min = j
        (Arr[i], Arr[min]) = (Arr[min], Arr[i])


def selectionSort2(Arr):
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
    for i in range(len(Arr)):
        swapped = False
        for j in range(len(Arr)-1-i):
            if Arr[j] > Arr[j+1]:
                swapped = True
                (Arr[j], Arr[j+1]) = (Arr[j+1], Arr[j])
        if not swapped:
            return


def bubbleSort2(Arr):
    global total
    for i in range(len(Arr)):
        swapped = False
        for j in range(len(Arr)-1-i):
            if Arr[j] > Arr[j+1]:
                swapped = True
                (Arr[j], Arr[j+1]) = (Arr[j+1], Arr[j])
                total += 1
            total += 1
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


def heap2(Arr, n, i):
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
        heap2(Arr, n, largest)


def heapSort(Arr):
    for i in range(len(Arr)//2-1, -1, -1):
        heap(Arr, len(Arr), i)
    for i in range(len(Arr)-1, 0, -1):
        (Arr[i], Arr[0]) = (Arr[0], Arr[i])
        heap(Arr, i, 0)


def heapSort2(Arr):
    global total
    for i in range(len(Arr)//2-1, -1, -1):
        heap2(Arr, len(Arr), i)
    for i in range(len(Arr)-1, 0, -1):
        (Arr[i], Arr[0]) = (Arr[0], Arr[i])
        total += 1
        heap2(Arr, i, 0)

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


def partition(Arr, begin, end, med):
    pivot = Arr[end]
    if med:
        pivot = Arr[int(round((begin+end))/2)]
    i = begin-1
    for j in range(begin, end):
        if Arr[j] <= pivot:
            i += 1
            (Arr[i], Arr[j]) = (Arr[j], Arr[i])
    (Arr[i+1], Arr[end]) = (Arr[end], Arr[i+1])
    return i+1


def partition2(Arr, begin, end, med):
    global total
    pivot = Arr[end]
    if med:
        pivot = Arr[int(round((begin+end))/2)]
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
        pivot = partition(Arr, start, end, False)
        quickSort(Arr, start, pivot-1)
        quickSort(Arr, pivot+1, end)


def quickSort2(Arr, start, end):
    if start < end:
        pivot = partition2(Arr, start, end, False)
        quickSort2(Arr, start, pivot-1)
        quickSort2(Arr, pivot+1, end)

# Quick Sort - pivot=medium


def quickSortMedium(Arr, start, end):
    if start < end:
        pivot = partition(Arr, start, end, True)
        quickSort(Arr, start, pivot-1)
        quickSort(Arr, pivot+1, end)


def quickSortMedium2(Arr, start, end):
    if start < end:
        pivot = partition2(Arr, start, end, True)
        quickSort2(Arr, start, pivot-1)
        quickSort2(Arr, pivot+1, end)

# Wykres czasu sortowania list od liczby elementów (algorytmy)


def wykr1(f):
    global Arr
    flag = True
    if f.__name__ == "quickSort" or f.__name__ == "quickSortMedium":
        flag = False
    print(f.__name__+":\n")
    x1, x2, x3, x4, x5 = [], [], [], [], []
    y1, y2, y3, y4, y5 = [], [], [], [], []
    plt.plot()
    for i in range(1000, 10001, 1000):
        Arr = incr(i)
        result = 0
        for _ in range(10):
            start = timer()
            if flag:
                f(Arr)
            else:
                f(Arr, 0, len(Arr)-1)
            end = timer()
            result += (end-start)
        result /= 10
        x1.append(i)
        y1.append(result*1000)
        print(f"Rosnąca {i}: {result*1000} milisekund")
    plt.plot(x1, y1, label="rosnąca", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        Arr = deincr(i)
        result = 0
        for _ in range(10):
            start = timer()
            if flag:
                f(Arr)
            else:
                f(Arr, 0, len(Arr)-1)
            end = timer()
            result += (end-start)
        result /= 10
        x2.append(i)
        y2.append(result*1000)
        print(f"Malejąca {i}: {result*1000} milisekund")
    plt.plot(x2, y2, label="malejąca", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        Arr = ashape(i)
        result = 0
        for _ in range(10):
            start = timer()
            if flag:
                f(Arr)
            else:
                f(Arr, 0, len(Arr)-1)
            end = timer()
            result += (end-start)
        result /= 10
        x3.append(i)
        y3.append(result*1000)
        print(f"A-kształtna {i}: {result*1000} milisekund")
    plt.plot(x3, y3, label="A-kształt", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        Arr = vshape(i)
        result = 0
        for _ in range(10):
            start = timer()
            if flag:
                f(Arr)
            else:
                f(Arr, 0, len(Arr)-1)
            end = timer()
            result += (end-start)
        result /= 10
        x4.append(i)
        y4.append(result*1000)
        print(f"V-kształtna {i}: {result*1000} milisekund")
    plt.plot(x4, y4, label="V-kształt", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        result = 0
        for _ in range(10):
            Arr = randomowa(i)
            for o in range(10):
                start = timer()
                if flag:
                    f(Arr)
                else:
                    f(Arr, 0, len(Arr)-1)
                end = timer()
                result += (end-start)
        result /= 100  # type: ignore
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
        writer.writerow(["Elementy listy", "Rosnaca", "Malejaca",
                        "A-ksztaltna", "V-ksztaltna", "Losowa"])
        for i in range(10):
            writer.writerow([(i+1)*100, round(y1[i], 2), round(y2[i], 2),
                            round(y3[i], 2), round(y4[i], 2), round(y5[i], 2)])

# Wykres czasu sortowania list od liczby elementów (rodzaje list)


def wykr2(f):
    global Arr
    n = 10
    match f.__name__:
        case "incr":
            print("Rosnąca:\n")
        case "deincr":
            print("malejąca:\n")
        case "ashape":
            print("A-kształtna:\n")
        case "vshape":
            print("V-kształtna:\n")
        case "randomowa":
            print("Losowa:\n")
            n = 100
        case _:
            print("Nie ma takiej funkcji")
            return
    x1, x2, x3, x4, x5, x6, x7 = [], [], [], [], [], [], []
    y1, y2, y3, y4, y5, y6, y7 = [], [], [], [], [], [], []
    plt.plot()
    for i in range(1000, 10001, 1000):
        result = 0
        if f.__name__ == "randomowa":
            for _ in range(10):
                Arr = f(i)
                for o in range(10):
                    start = timer()
                    insertionSort(Arr)
                    end = timer()
                    result += (end-start)
        else:
            Arr = f(i)
            for _ in range(n):
                start = timer()
                insertionSort(Arr)
                end = timer()
                result += (end-start)
        result /= n
        x1.append(i)
        y1.append(result*1000)
        print(f"Insertion sort {i}: {result*1000} milisekund")
    plt.plot(x1, y1, label="Insertion sort", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        result = 0
        if f.__name__ == "randomowa":
            for _ in range(10):
                Arr = f(i)
                for o in range(10):
                    start = timer()
                    selectionSort(Arr)
                    end = timer()
                    result += (end-start)
        else:
            Arr = f(i)
            for _ in range(n):
                start = timer()
                selectionSort(Arr)
                end = timer()
                result += (end-start)
        result /= n
        x2.append(i)
        y2.append(result*1000)
        print(f"Selection sort {i}: {result*1000} milisekund")
    plt.plot(x2, y2, label="Selection sort", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        result = 0
        if f.__name__ == "randomowa":
            for _ in range(10):
                Arr = f(i)
                for o in range(10):
                    start = timer()
                    bubbleSort(Arr)
                    end = timer()
                    result += (end-start)
        else:
            Arr = f(i)
            for _ in range(n):
                start = timer()
                bubbleSort(Arr)
                end = timer()
                result += (end-start)
        result /= n
        x3.append(i)
        y3.append(result*1000)
        print(f"Bubble sort {i}: {result*1000} milisekund")
    plt.plot(x3, y3, label="Bubble sort", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        result = 0
        if f.__name__ == "randomowa":
            for _ in range(10):
                Arr = f(i)
                for o in range(10):
                    start = timer()
                    heapSort(Arr)
                    end = timer()
                    result += (end-start)
        else:
            Arr = f(i)
            for _ in range(n):
                start = timer()
                heapSort(Arr)
                end = timer()
                result += (end-start)
        result /= n
        x4.append(i)
        y4.append(result*1000)
        print(f"Heap sort {i}: {result*1000} milisekund")
    plt.plot(x4, y4, label="Heap sort", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        result = 0
        if f.__name__ == "randomowa":
            for _ in range(10):
                Arr = f(i)
                for o in range(10):
                    start = timer()
                    mergeSort(Arr)
                    end = timer()
                    result += (end-start)
        else:
            Arr = f(i)
            for _ in range(n):
                start = timer()
                mergeSort(Arr)
                end = timer()
                result += (end-start)
        result /= n
        x5.append(i)
        y5.append(result*1000)
        print(f"Merge sort {i}: {result*1000} milisekund")
    plt.plot(x5, y5, label="Merge sort", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        result = 0
        if f.__name__ == "randomowa":
            for _ in range(10):
                Arr = f(i)
                for o in range(10):
                    start = timer()
                    quickSort(Arr, 0, len(Arr)-1)
                    end = timer()
                    result += (end-start)
        else:
            Arr = f(i)
            for _ in range(n):
                start = timer()
                quickSort(Arr, 0, len(Arr)-1)
                end = timer()
                result += (end-start)
        result /= n
        x6.append(i)
        y6.append(result*1000)
        print(f"Quicksort {i}: {result*1000} milisekund")
    plt.plot(x6, y6, label="Quicksort", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        result = 0
        if f.__name__ == "randomowa":
            for _ in range(10):
                Arr = f(i)
                for o in range(10):
                    start = timer()
                    quickSortMedium(Arr, 0, len(Arr)-1)
                    end = timer()
                    result += (end-start)
        else:
            Arr = f(i)
            for _ in range(n):
                start = timer()
                quickSortMedium(Arr, 0, len(Arr)-1)
                end = timer()
                result += (end-start)
        result /= n
        x7.append(i)
        y7.append(result*1000)
        print(f"Quicksort (pivot=medium) {i}: {result*1000} milisekund")
    plt.plot(x7, y7, label="QuicksortMedium", alpha=0.7)
    plt.xlabel("Elementy listy")
    plt.ylabel("Czas sortowania")
    plt.title(f'Złożoność obliczeniowa {f.__name__}')
    plt.legend(loc='upper left')
    plt.savefig(f'Wykres2/{f.__name__}.png', bbox_inches='tight')
    print("\nWykres wygenerowany\n\n")
    plt.clf()
    with open(f"Wykres2\\{f.__name__}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Elementy listy", "Insertion", "Selection",
                        "Bubble", "Heap", "Merge", "Quick", "QuickIter"])
        for i in range(10):
            writer.writerow([(i+1)*100, round(y1[i], 2), round(y2[i], 2), round(
                y3[i], 2), round(y4[i], 2), round(y5[i], 2), round(y6[i], 2), round(y7[i], 2)])

# Wykres liczby operacji k (porównań i zamian) od liczby elementów (rodzaje list)


def wykr3(f):
    global total
    n = 1
    flag = True
    match f.__name__:
        case "incr":
            print("Rosnąca:\n")
        case "deincr":
            print("Malejąca:\n")
        case "ashape":
            print("A-kształtna:\n")
        case "vshape":
            print("V-kształtna:\n")
        case "randomowa":
            print("Losowa:\n")
            n = 10
            flag = False
        case _:
            print("Nie ma takiej funkcji")
            return
    x1, x2, x3, x4, x5, x6, x7 = [], [], [], [], [], [], []
    y1, y2, y3, y4, y5, y6, y7 = [], [], [], [], [], [], []
    plt.plot()
    for i in range(1000, 10001, 1000):
        total = 0
        if flag:
            Arr = f(i)
            for _ in range(n):
                insertionSort2(Arr)
        else:
            for _ in range(n):
                Arr = f(i)
                insertionSort2(Arr)
        x1.append(i)
        y1.append(total//n)
        print(f"Insertion sort {i}: {total//n} operacji")
    plt.plot(x1, y1, label="Insertion sort", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        total = 0
        if flag:
            Arr = f(i)
            for _ in range(n):
                selectionSort2(Arr)
        else:
            for _ in range(n):
                Arr = f(i)
                selectionSort2(Arr)
        x2.append(i)
        y2.append(total//n)
        print(f"Selection sort {i}: {total//n} operacji")
    plt.plot(x2, y2, label="Selection sort", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        total = 0
        if flag:
            Arr = f(i)
            for _ in range(n):
                bubbleSort2(Arr)
        else:
            for _ in range(n):
                Arr = f(i)
                bubbleSort2(Arr)
        x3.append(i)
        y3.append(total//n)
        print(f"Bubble sort {i}: {total//n} operacji")
    plt.plot(x3, y3, label="Bubble sort", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        total = 0
        if flag:
            Arr = f(i)
            for _ in range(n):
                heapSort2(Arr)
        else:
            for _ in range(n):
                Arr = f(i)
                heapSort2(Arr)
        x4.append(i)
        y4.append(total//n)
        print(f"Heap sort {i}: {total//n} operacji")
    plt.plot(x4, y4, label="Heap sort", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        total = 0
        if flag:
            Arr = f(i)
            for _ in range(n):
                mergeSort2(Arr)
        else:
            for _ in range(n):
                Arr = f(i)
                mergeSort2(Arr)
        x5.append(i)
        y5.append(total//n)
        print(f"Merge sort {i}: {total//n} operacji")
    plt.plot(x5, y5, label="Merge sort", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        total = 0
        if flag:
            Arr = f(i)
            for _ in range(n):
                quickSort2(Arr, 0, len(Arr)-1)
        else:
            for _ in range(n):
                Arr = f(i)
                quickSort2(Arr, 0, len(Arr)-1)
        x6.append(i)
        y6.append(total//n)
        print(f"Quicksort {i}: {total//n} operacji")
    plt.plot(x6, y6, label="Quicksort", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        total = 0
        if flag:
            Arr = f(i)
            for _ in range(n):
                quickSortMedium2(Arr, 0, len(Arr)-1)
        else:
            for _ in range(n):
                Arr = f(i)
                quickSortMedium2(Arr, 0, len(Arr)-1)
        x7.append(i)
        y7.append(total//n)
        print(f"Quicksort (pivot=medium) {i}: {total//n} operacji")
    plt.plot(x7, y7, label="QuicksortMedium", alpha=0.7)
    plt.xlabel("Elementy listy")
    plt.ylabel("Liczba operacji")
    plt.title(f'Złożoność obliczeniowa {f.__name__} (operacje)')
    plt.legend(loc='upper left')
    plt.savefig(f'Wykres3/{f.__name__}.png', bbox_inches='tight')
    print("\nWykres wygenerowany\n\n")
    plt.clf()
    with open(f"Wykres3\\{f.__name__}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Elementy listy", "Insertion", "Selection",
                        "Bubble", "Heap", "Merge", "Quick", "Quick medium"])
        for i in range(10):
            writer.writerow([(i+1)*1000, y1[i], y2[i], y3[i],
                            y4[i], y5[i], y6[i], y7[i]])

# Wykres liczby operacji k (porównań i zamian) od liczby elementów (algorytmy)


def wykr4(f):
    global total
    func, fname = "", ""
    flag = True
    match f.__name__:
        case "insertionSort2":
            fname = "insertionSort"
            func = "Insertion sort"
        case "selectionSort2":
            fname = "selectionSort"
            func = "Selection sort"
        case "bubbleSort2":
            fname = "bubbleSort"
            func = "Bubble sort"
        case "heapSort2":
            fname = "heapSort"
            func = "Heap sort"
        case "mergeSort2":
            fname = "mergeSort"
            func = "Merge sort"
        case "quickSort2":
            fname = "quickSort"
            func = "Quick sort"
            flag = False
        case "quickSortMedoim2":
            fname = "quickSortMedium"
            func = "Quick sort (pivot=medium)"
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
    plt.plot(x3, y3, label="A-ksztalt", alpha=0.7)
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
    plt.plot(x4, y4, label="V-ksztalt", alpha=0.7)
    print(" ")
    for i in range(1000, 10001, 1000):
        Arr = randomowa(i)
        total = 0
        for _ in range(100):
            if flag:
                f(Arr)
            else:
                f(Arr, 0, len(Arr)-1)
        x5.append(i)
        y5.append(total//100)
        print(f"Losowa {i}: {total//100} operacji")
    plt.plot(x5, y5, label="losowa", alpha=0.7)
    plt.xlabel("Elementy listy")
    plt.ylabel("Liczba operacji")
    plt.title(f'Zlozonosc obliczeniowa {f.__name__}')
    plt.legend(loc='upper left')
    plt.savefig(f'Wykres4/{fname}.png', bbox_inches='tight')
    print("\nWykres wygenerowany\n\n")
    plt.clf()
    with open(f"Wykres4\\{fname}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Elementy listy", "Rosnąca", "Malejąca",
                        "A-kształtna", "V-kształtna", "Losowa"])
        for i in range(10):
            writer.writerow([(i+1)*1000, y1[i], y2[i], y3[i], y4[i], y5[i]])


flag1, flag2, flag3, flag4, flag5 = False, False, False, False, False
print("Które wykresy chcesz wygenerować?")
print(
    "1. Wykres czasu sortowania list od liczby elementów (algorytmy)\n[Y/N]")
tmp = input()
if tmp.upper() == "Y":
    flag1 = True
print(
    "2. Wykres czasu sortowania list od liczby elementów (rodzaje list)\n[Y/N]")
tmp = input()
if tmp.upper() == "Y":
    flag2 = True
print(
    "3. Wykres liczby operacji k (porównań i zamian) od liczby elementów (rodzaje list)\n[Y/N]")
tmp = input()
if tmp.upper() == "Y":
    flag3 = True
print(
    "4. Wykres liczby operacji k (porównań i zamian) od liczby elementów (algorytmy)\n[Y/N]")
tmp = input()
if tmp.upper() == "Y":
    flag4 = True
print("Czy chcesz zamknąć system po zakończeniu?\n[Y/N]")
tmp = input()
if tmp.upper() == "Y":
    flag5 = True

if flag1:
    wykr1(insertionSort)
    wykr1(selectionSort)
    wykr1(bubbleSort)
    wykr1(heapSort)
    wykr1(mergeSort)
    wykr1(quickSort)
    wykr1(quickSortMedium)
if flag2:
    wykr2(incr)
    wykr2(deincr)
    wykr2(ashape)
    wykr2(vshape)
    wykr2(randomowa)
if flag3:
    wykr3(incr)
    wykr3(deincr)
    wykr3(ashape)
    wykr3(vshape)
    wykr3(randomowa)
if flag4:
    wykr4(insertionSort2)
    wykr4(selectionSort2)
    wykr4(bubbleSort2)
    wykr4(heapSort2)
    wykr4(mergeSort2)
    wykr4(quickSort2)
if flag5:
    os.system("shutdown /s /t 1")
