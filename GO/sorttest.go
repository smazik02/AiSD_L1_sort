package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

var total = 0

// Generatory list
func incr(n int) []int {
	Arr := make([]int, n)
	for i := 0; i < n; i++ {
		Arr[i] = i
	}
	return Arr
}
func deincr(n int) []int {
	Arr := make([]int, n)
	for i := 0; i < n; i++ {
		Arr[i] = n - i - 1
	}
	return Arr
}
func ashape(n int) []int {
	var x int = n / 2
	left := make([]int, x)
	right := make([]int, x)
	for i := 0; i < x; i++ {
		left[i] = i
	}
	for i := 0; i < x; i++ {
		right[i] = x - i - 1
	}
	return append(left, right...)
}
func vshape(n int) []int {
	var x int = n / 2
	left := make([]int, x)
	right := make([]int, x)
	for i := 0; i < x; i++ {
		left[i] = x - i - 1
	}
	for i := 0; i < x; i++ {
		right[i] = i
	}
	return append(left, right...)
}
func random(n int) []int {
	Arr := make([]int, n)
	for i := 0; i < n; i++ {
		Arr[i] = rand.Intn(n)
	}
	return Arr
}

// Insertion sort
func insertionSort(Arr []int) []int {
	for i := 1; i < len(Arr); i++ {
		key := Arr[i]
		j := i - 1
		for j >= 0 && Arr[j] > key {
			Arr[j+1] = Arr[j]
			j--
		}
		Arr[j+1] = key
	}
	return Arr
}
func insertionSort2(Arr []int) []int {
	for i := 1; i < len(Arr); i++ {
		key := Arr[i]
		j := i - 1
		for j >= 0 && Arr[j] > key {
			total++
			Arr[j+1] = Arr[j]
			total++
			j--
		}
		total++
		Arr[j+1] = key
		total++
	}
	return Arr
}

// Selection sort
func selectionSort(Arr []int) []int {
	for i := 0; i < len(Arr); i++ {
		min := i
		for j := i + 1; j < len(Arr); j++ {
			if Arr[j] < Arr[min] {
				min = j
			}
		}
		Arr[i], Arr[min] = Arr[min], Arr[i]
	}
	return Arr
}
func selectionSort2(Arr []int) []int {
	for i := 0; i < len(Arr); i++ {
		min := i
		for j := i + 1; j < len(Arr); j++ {
			if Arr[j] < Arr[min] {
				min = j
			}
			total++
		}
		Arr[i], Arr[min] = Arr[min], Arr[i]
		total++
	}
	return Arr
}

// Bubble sort
func bubbleSort(Arr []int) []int {
	for i := 0; i < len(Arr); i++ {
		swapped := false
		for j := 0; j < len(Arr)-1-i; j++ {
			if Arr[j] > Arr[j+1] {
				swapped = true
				Arr[j], Arr[j+1] = Arr[j+1], Arr[j]
			}
		}
		if !swapped {
			return Arr
		}
	}
	return Arr
}
func bubbleSort2(Arr []int) []int {
	for i := 0; i < len(Arr); i++ {
		swapped := false
		for j := 0; j < len(Arr)-1-i; j++ {
			if Arr[j] > Arr[j+1] {
				swapped = true
				Arr[j], Arr[j+1] = Arr[j+1], Arr[j]
				total++
			}
			total++
		}
		if !swapped {
			return Arr
		}
	}
	return Arr
}

// Heap sort
func heap(Arr []int, n int, i int) []int {
	largest := i
	l := 2*i + 1
	r := 2*i + 2
	if l < n && Arr[i] < Arr[l] {
		largest = l
	}
	if r < n && Arr[largest] < Arr[r] {
		largest = r
	}
	if largest != i {
		Arr[i], Arr[largest] = Arr[largest], Arr[i]
		Arr = heap(Arr, n, largest)
	}
	return Arr
}
func heap2(Arr []int, n int, i int) []int {
	largest := i
	l := 2*i + 1
	r := 2*i + 2
	if l < n && Arr[i] < Arr[l] {
		largest = l
	}
	total++
	if r < n && Arr[largest] < Arr[r] {
		largest = r
	}
	total++
	if largest != i {
		Arr[i], Arr[largest] = Arr[largest], Arr[i]
		total++
		Arr = heap(Arr, n, largest)
	}
	return Arr
}
func heapSort(Arr []int) []int {
	for i := len(Arr)/2 - 1; i >= 0; i-- {
		Arr = heap(Arr, len(Arr), i)
	}
	for i := len(Arr) - 1; i > 0; i-- {
		Arr[i], Arr[0] = Arr[0], Arr[i]
		Arr = heap(Arr, i, 0)
	}
	return Arr
}
func heapSort2(Arr []int) []int {
	for i := len(Arr)/2 - 1; i >= 0; i-- {
		Arr = heap(Arr, len(Arr), i)
	}
	for i := len(Arr) - 1; i > 0; i-- {
		Arr[i], Arr[0] = Arr[0], Arr[i]
		total++
		Arr = heap(Arr, i, 0)
	}
	return Arr
}

// Merge sort
func mergeSort(Arr []int) []int {
	if len(Arr) > 1 {
		var middle int = len(Arr) / 2
		L := Arr[:middle]
		R := Arr[middle:]
		mergeSort(L)
		mergeSort(R)
		i := 0
		j := 0
		k := 0

		for i < len(L) && j < len(R) {
			if L[i] <= R[j] {
				Arr[k] = L[i]
				i++
			} else {
				Arr[k] = R[j]
				j++
			}
			k++
		}

		for i < len(L) {
			Arr[k] = L[i]
			i++
			k++
		}

		for j < len(R) {
			Arr[k] = R[j]
			j++
			k++
		}
	}
	return Arr
}
func mergeSort2(Arr []int) []int {
	if len(Arr) > 1 {
		var middle int = len(Arr) / 2
		L := Arr[:middle]
		R := Arr[middle:]
		mergeSort(L)
		mergeSort(R)
		i := 0
		j := 0
		k := 0

		for i < len(L) && j < len(R) {
			if L[i] <= R[j] {
				Arr[k] = L[i]
				i++
			} else {
				Arr[k] = R[j]
				j++
			}
			total++
			k++
		}

		for i < len(L) {
			Arr[k] = L[i]
			i++
			k++
		}

		for j < len(R) {
			Arr[k] = R[j]
			j++
			k++
		}
	}
	return Arr
}

// Quicksort
func partition(Arr []int, begin, end int) (int, []int) {
	pivot := Arr[end]
	i := begin - 1
	for j := begin; j < end; j++ {
		if Arr[j] <= pivot {
			i++
			Arr[i], Arr[j] = Arr[j], Arr[i]
		}
	}
	Arr[i+1], Arr[end] = Arr[end], Arr[i+1]
	return i + 1, Arr
}
func partition2(Arr []int, begin, end int) (int, []int) {
	pivot := Arr[end]
	i := begin - 1
	for j := begin; j < end; j++ {
		if Arr[j] <= pivot {
			i++
			Arr[i], Arr[j] = Arr[j], Arr[i]
			total++
		}
		total++
	}
	Arr[i+1], Arr[end] = Arr[end], Arr[i+1]
	total++
	return i + 1, Arr
}
func quickSort(Arr []int, start, end int) []int {
	if start < end {
		pivot, Arr := partition(Arr, start, end)
		quickSort(Arr, start, pivot-1)
		quickSort(Arr, pivot+1, end)
	}
	return Arr
}
func quickSort2(Arr []int, start, end int) []int {
	if start < end {
		pivot, Arr := partition2(Arr, start, end)
		quickSort2(Arr, start, pivot-1)
		quickSort2(Arr, pivot+1, end)
	}
	return Arr
}
func quickSortStart(Arr []int) []int {
	return quickSort(Arr, 0, len(Arr)-1)
}
func quickSortStart2(Arr []int) []int {
	return quickSort2(Arr, 0, len(Arr)-1)
}

// Wykres czasu sortowania list od liczby elementów (algorytmy)
func wykr1(f func([]int) []int, name string, rep int) {
	fmt.Println(name)
	for i := rep; i <= rep*10; i += rep {
		var result float64 = 0
		for j := 0; j < 10; j++ {
			Arr := incr(i)
			start := time.Now()
			_ = f(Arr)
			duration := time.Since(start)
			result += float64(duration.Nanoseconds())
		}
		result /= 10
		fmt.Printf("Rosnąca %v: %v ms\n", i, result/1000000)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		var result float64 = 0
		for j := 0; j < 10; j++ {
			Arr := deincr(i)
			start := time.Now()
			_ = f(Arr)
			duration := time.Since(start)
			result += float64(duration.Nanoseconds())
		}
		result /= 10
		fmt.Printf("Malejąca %v: %v ms\n", i, result/1000000)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		var result float64 = 0
		for j := 0; j < 10; j++ {
			Arr := ashape(i)
			start := time.Now()
			_ = f(Arr)
			duration := time.Since(start)
			result += float64(duration.Nanoseconds())
		}
		result /= 10
		fmt.Printf("A-kształtna %v: %v ms\n", i, result/1000000)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		var result float64 = 0
		for j := 0; j < 10; j++ {
			Arr := vshape(i)
			start := time.Now()
			_ = f(Arr)
			duration := time.Since(start)
			result += float64(duration.Nanoseconds())
		}
		result /= 10
		fmt.Printf("V-kształtna %v: %v ms\n", i, result/1000000)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		var result float64 = 0
		for j := 0; j < 100; j++ {
			Arr := random(i)
			start := time.Now()
			_ = f(Arr)
			duration := time.Since(start)
			result += float64(duration.Nanoseconds())
		}
		result /= 100
		fmt.Printf("Losowa %v: %v ms\n", i, result/1000000)
	}
}

// Wykres czasu sortowania list od liczby elementów (rodzaje list)
func wykr2(f func(int) []int, name string, rep int) {
	n := 10
	if name == "random" {
		n = 100
	}
	fmt.Println(name)
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		var result float64 = 0
		for j := 0; j < n; j++ {
			Arr := f(i)
			start := time.Now()
			_ = insertionSort(Arr)
			duration := time.Since(start)
			result += float64(duration.Nanoseconds())
		}
		result /= float64(n)
		fmt.Printf("Insertion sort %v: %v ms\n", i, result/1000000)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		var result float64 = 0
		for j := 0; j < n; j++ {
			Arr := f(i)
			start := time.Now()
			_ = selectionSort(Arr)
			duration := time.Since(start)
			result += float64(duration.Nanoseconds())
		}
		result /= float64(n)
		fmt.Printf("Selection sort %v: %v ms\n", i, result/1000000)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		var result float64 = 0
		for j := 0; j < n; j++ {
			Arr := f(i)
			start := time.Now()
			_ = bubbleSort(Arr)
			duration := time.Since(start)
			result += float64(duration.Nanoseconds())
		}
		result /= float64(n)
		fmt.Printf("Bubble sort %v: %v ms\n", i, result/1000000)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		var result float64 = 0
		for j := 0; j < n; j++ {
			Arr := f(i)
			start := time.Now()
			_ = heapSort(Arr)
			duration := time.Since(start)
			result += float64(duration.Nanoseconds())
		}
		result /= float64(n)
		fmt.Printf("Heap sort %v: %v ms\n", i, result/1000000)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		var result float64 = 0
		for j := 0; j < n; j++ {
			Arr := f(i)
			start := time.Now()
			_ = mergeSort(Arr)
			duration := time.Since(start)
			result += float64(duration.Nanoseconds())
		}
		result /= float64(n)
		fmt.Printf("Merge sort %v: %v ms\n", i, result/1000000)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		var result float64 = 0
		for j := 0; j < n; j++ {
			start := time.Now()
			Arr := f(i)
			_ = quickSortStart(Arr)
			duration := time.Since(start)
			result += float64(duration.Nanoseconds())
		}
		result /= float64(n)
		fmt.Printf("Quicksort %v: %v operacji\n", i, result/1000000)
	}
	fmt.Println(" ")
}

// Wykres liczby operacji k (porównań i zamian) od liczby elementów (rodzaje list)
func wykr3(f func(int) []int, name string, rep int) {
	n := 1
	if name == "random" {
		n = 10
	}
	fmt.Println(name)
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		total = 0
		for j := 0; j < n; j++ {
			Arr := f(i)
			_ = insertionSort2(Arr)
		}
		fmt.Printf("Insertion sort %v: %v operacji\n", i, total/n)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		total = 0
		for j := 0; j < n; j++ {
			Arr := f(i)
			_ = selectionSort2(Arr)
		}
		fmt.Printf("Selection sort %v: %v operacji\n", i, total/n)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		total = 0
		for j := 0; j < n; j++ {
			Arr := f(i)
			_ = bubbleSort2(Arr)
		}
		fmt.Printf("Bubble sort %v: %v operacji\n", i, total/n)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		total = 0
		for j := 0; j < n; j++ {
			Arr := f(i)
			_ = heapSort2(Arr)
		}
		fmt.Printf("Heap sort %v: %v operacji\n", i, total/n)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		total = 0
		for j := 0; j < n; j++ {
			Arr := f(i)
			_ = mergeSort2(Arr)
		}
		fmt.Printf("Merge sort %v: %v operacji\n", i, total/n)
	}
	fmt.Println(" ")
	for i := rep; i <= rep*10; i += rep {
		total = 0
		for j := 0; j < n; j++ {
			Arr := f(i)
			_ = quickSortStart2(Arr)
		}
		fmt.Printf("Quicksort %v: %v operacji\n", i, total/n)
	}
	fmt.Println(" ")
}

func main() {
	flag1, flag2, flag3 := false, false, false
	tmp := ""
	fmt.Println("Które wykresy chcesz wygenerować?")
	fmt.Println("1. Wykres czasu sortowania list od liczby elementów (algorytmy)\n[Y/N]")
	fmt.Scanln(&tmp)
	if strings.ToUpper(tmp) == "Y" {
		flag1 = true
	}
	fmt.Println("2. Wykres czasu sortowania list od liczby elementów (rodzaje list)\n[Y/N]")
	fmt.Scanln(&tmp)
	if strings.ToUpper(tmp) == "Y" {
		flag2 = true
	}
	fmt.Println("3. Wykres liczby operacji k (porównań i zamian) od liczby elementów (rodzaje list)\n[Y/N]")
	fmt.Scanln(&tmp)
	if strings.ToUpper(tmp) == "Y" {
		flag3 = true
	}
	if flag1 {
		wykr1(insertionSort, "Insertion Sort", 10000)
		wykr1(selectionSort, "Selection Sort", 10000)
		wykr1(bubbleSort, "Bubble Sort", 10000)
		wykr1(heapSort, "Heap Sort", 100000)
		wykr1(mergeSort, "Merge Sort", 100000)
		wykr1(quickSortStart, "Quicksort", 10000)
	}
	if flag2 {
		wykr2(incr, "Rosnąca", 10000)
		wykr2(deincr, "Malejąca", 10000)
		wykr2(ashape, "A-kształtna", 10000)
		wykr2(vshape, "V-kształtna", 10000)
		wykr2(random, "Losowa", 10000)
	}
	if flag3 {
		wykr3(incr, "Rosnąca", 10000)
		wykr3(deincr, "Malejąca", 10000)
		wykr3(ashape, "A-kształtna", 10000)
		wykr3(vshape, "V-kształtna", 10000)
		wykr3(random, "Losowa", 10000)
	}
}
