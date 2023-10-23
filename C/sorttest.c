#include <locale.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void swap(int* a, int* b);

void printArr(int Arr[], int n);

int* incr(int n);

int* deincr(int n);

int* ashape(int n);

int* vshape(int n);

int* randomowa(int n);

void insertionSort(int Arr[], int len);

void insertionSort2(int Arr[], int len, int* total);

void selectionSort(int Arr[], int len);

void selectionSort2(int Arr[], int len, int* total);

void bubbleSort(int Arr[], int len);

void bubbleSort2(int Arr[], int len, int* total);

void heap(int Arr[], int n, int i);

void heap2(int Arr[], int n, int i, int* total);

void heapSort(int Arr[], int len);

void heapSort2(int Arr[], int len, int* total);

void merge(int Arr[], int l, int m, int r);

void merge2(int Arr[], int l, int m, int r, int* total);

void mergeSort(int Arr[], int l, int r);

void mergeSort2(int Arr[], int l, int r, int* total);

void mergeSortStart(int Arr[], int len);

void mergeSortStart2(int Arr[], int len, int* total);

int partition(int Arr[], int begin, int end);

int partition2(int Arr[], int begin, int end, int* total);

void quickSort(int Arr[], int begin, int end);

void quickSort2(int Arr[], int begin, int end, int* total);

void quickSortStart(int Arr[], int len);

void quickSortStart2(int Arr[], int len, int* total);

void wykr1(void (*f)(int[], int), char name[], int rep);

void wykr2();

void wykr3();

void wykr4();

int main(void) {
    /*
    wykr1(insertionSort, "Insertion Sort", 10000);
    printf("\n\n");
    wykr1(selectionSort, "Selection Sort", 10000);
    printf("\n\n");
    wykr1(bubbleSort, "Bubble Sort", 10000);
    printf("\n\n");
    */
    wykr1(heapSort, "Heap Sort", 10000);
    printf("\n\n");
    wykr1(mergeSortStart, "Merge Sort", 10000);
    printf("\n\n");
    wykr1(quickSortStart, "Quicksort", 10000);
    return 0;
}

void wykr1(void (*f)(int[], int), char name[], int rep) {
    clock_t time;
    double result;
    printf("%s\n", name);
    for (int i = rep; i <= rep * 10; i += rep) {
        double result = 0;
        int* Arr;
        for (int j = 0; j < 10; j++) {
            Arr = incr(i);
            time = clock();
            (*f)(Arr, i);
            time = clock() - time;
            result += ((double)time) / CLOCKS_PER_SEC;
        }
        result /= 10;
        printf("Incrementing %d: %f ms\n", i, result * 1000);
    }
    printf("\n");
    for (int i = rep; i <= rep * 10; i += rep) {
        result = 0;
        int* Arr;
        for (int j = 0; j < 10; j++) {
            Arr = deincr(i);
            time = clock();
            (*f)(Arr, i);
            time = clock() - time;
            result += ((double)time) / CLOCKS_PER_SEC;
        }
        result /= 10;
        printf("Deincrementing %d: %f ms\n", i, result * 1000);
    }
    printf("\n");
    for (int i = rep; i <= rep * 10; i += rep) {
        result = 0;
        int* Arr;
        for (int j = 0; j < 10; j++) {
            Arr = ashape(i);
            time = clock();
            (*f)(Arr, i);
            time = clock() - time;
            result += ((double)time) / CLOCKS_PER_SEC;
        }
        result /= 10;
        printf("A-shaped %d: %f ms\n", i, result * 1000);
    }
    printf("\n");
    for (int i = rep; i <= rep * 10; i += rep) {
        result = 0;
        int* Arr;
        for (int j = 0; j < 10; j++) {
            Arr = vshape(i);
            time = clock();
            (*f)(Arr, i);
            time = clock() - time;
            result += ((double)time) / CLOCKS_PER_SEC;
        }
        result /= 10;
        printf("V-shaped %d: %f ms\n", i, result * 1000);
    }
    printf("\n");
    for (int i = rep; i <= rep * 10; i += rep) {
        result = 0;
        int* Arr;
        for (int j = 0; j < 10; j++) {
            Arr = randomowa(i);
            time = clock();
            (*f)(Arr, i);
            time = clock() - time;
            result += ((double)time) / CLOCKS_PER_SEC;
        }
        result /= 10;
        printf("Random %d: %f ms\n", i, result * 1000);
    }
}

void wykr2() {
}

void wykr3() {
}

void wykr4() {
}

void swap(int* a, int* b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void printArr(int Arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", Arr[i]);
    }
    printf("\n");
}

int* incr(int n) {
    int* Arr = malloc(n * sizeof(int));
    if (!Arr) return NULL;
    for (int i = 0; i < n; i++) {
        Arr[i] = i;
    }
    return Arr;
}

int* deincr(int n) {
    int* Arr = malloc(n * sizeof(int));
    if (!Arr) return NULL;
    for (int i = 0; i < n; i++) {
        Arr[i] = n - i - 1;
    }
    return Arr;
}

int* ashape(int n) {
    int* Arr = malloc(n * sizeof(int));
    if (!Arr) return NULL;
    for (int i = 0; i < n / 2; i++) {
        Arr[i] = i;
    }
    for (int i = n / 2; i < n; i++) {
        Arr[i] = n - i - 1;
    }
    return Arr;
}

int* vshape(int n) {
    int* Arr = malloc(n * sizeof(int));
    if (!Arr) return NULL;
    for (int i = 0; i < n / 2; i++) {
        Arr[i] = n / 2 - i - 1;
    }
    for (int i = n / 2; i < n; i++) {
        Arr[i] = i - (n / 2);
    }
    return Arr;
}

int* randomowa(int n) {
    int* Arr = malloc(n * sizeof(int));
    if (!Arr) return NULL;
    for (int i = 0; i < n; i++) {
        Arr[i] = i;
    }
    srand(time(NULL));
    for (int i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        swap(&Arr[i], &Arr[j]);
    }
    return Arr;
}

void insertionSort(int Arr[], int len) {
    int key, j;
    for (int i = 1; i < len; i++) {
        key = Arr[i];
        j = i - 1;
        while (j >= 0 && Arr[j] > key) {
            swap(&Arr[j + 1], &Arr[j]);
            j--;
        }
        Arr[j + 1] = key;
    }
}

void insertionSort2(int Arr[], int len, int* total) {
    int key, j;
    for (int i = 1; i < len; i++) {
        key = Arr[i];
        j = i - 1;
        while (j >= 0 && Arr[j] > key) {
            *total++;
            swap(&Arr[j + 1], &Arr[j]);
            *total++;
            j--;
        }
        *total++;
        Arr[j + 1] = key;
        *total++;
    }
}

void selectionSort(int Arr[], int len) {
    int min;
    for (int i = 0; i < len; i++) {
        min = i;
        for (int j = i + 1; j < len; j++) {
            if (Arr[j] < Arr[min]) {
                min = j;
            }
        }
        swap(&Arr[i], &Arr[min]);
    }
}

void selectionSort2(int Arr[], int len, int* total) {
    int min;
    for (int i = 0; i < len; i++) {
        min = i;
        for (int j = i + 1; j < len; j++) {
            if (Arr[j] < Arr[min]) {
                min = j;
            }
            *total++;
        }
        swap(&Arr[i], &Arr[min]);
        *total++;
    }
}

void bubbleSort(int Arr[], int len) {
    bool swapped;
    for (int i = 0; i < len; i++) {
        swapped = false;
        for (int j = 0; j < len - 1 - i; j++) {
            if (Arr[j] > Arr[j + 1]) {
                swapped = true;
                swap(&Arr[j], &Arr[j + 1]);
            }
        }
        if (!swapped) {
            return;
        }
    }
}

void bubbleSort2(int Arr[], int len, int* total) {
    bool swapped;
    for (int i = 0; i < len; i++) {
        swapped = false;
        for (int j = 0; j < len - 1 - i; j++) {
            if (Arr[j] > Arr[j + 1]) {
                swapped = true;
                swap(&Arr[j], &Arr[j + 1]);
                *total++;
            }
            *total++;
        }
        if (!swapped) {
            return;
        }
    }
}

void heap(int Arr[], int n, int i) {
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;
    if (l < n && Arr[i] < Arr[l]) {
        largest = l;
    }
    if (r < n && Arr[largest] < Arr[r]) {
        largest = r;
    }
    if (largest != i) {
        swap(&Arr[i], &Arr[largest]);
        heap(Arr, n, largest);
    }
}

void heap2(int Arr[], int n, int i, int* total) {
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;
    if (l < n && Arr[i] < Arr[l]) {
        largest = l;
    }
    *total++;
    if (r < n && Arr[largest] < Arr[r]) {
        largest = r;
    }
    *total++;
    if (largest != i) {
        swap(&Arr[i], &Arr[largest]);
        *total++;
        heap2(Arr, n, largest, total);
    }
}

void heapSort(int Arr[], int len) {
    for (int i = len / 2 - 1; i > -1; i--) {
        heap(Arr, len, i);
    }
    for (int i = len - 1; i > 0; i--) {
        swap(&Arr[i], &Arr[0]);
        heap(Arr, i, 0);
    }
}

void heapSort2(int Arr[], int len, int* total) {
    for (int i = len / 2 - 1; i > -1; i--) {
        heap2(Arr, len, i, total);
    }
    for (int i = len - 1; i > 0; i--) {
        swap(&Arr[i], &Arr[0]);
        *total++;
        heap2(Arr, i, 0, total);
    }
}

void merge(int Arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    int* L = malloc(n1 * sizeof(int));
    int* R = malloc(n2 * sizeof(int));

    for (int i = 0; i < n1; i++) {
        L[i] = Arr[l + i];
    }
    for (int j = 0; j < n2; j++) {
        R[j] = Arr[m + 1 + j];
    }

    int i = 0;
    int j = 0;
    int k = l;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            Arr[k++] = L[i++];
        } else {
            Arr[k++] = R[j++];
        }
    }

    while (i < n1) {
        Arr[k++] = L[i++];
    }

    while (j < n2) {
        Arr[k++] = R[j++];
    }

    free(L);
    free(R);
}

void merge2(int Arr[], int l, int m, int r, int* total) {
    int n1 = m - l + 1;
    int n2 = r - m;

    int* L = malloc(n1 * sizeof(int));
    int* R = malloc(n2 * sizeof(int));

    for (int i = 0; i < n1; i++) {
        L[i] = Arr[l + i];
    }
    for (int j = 0; j < n2; j++) {
        R[j] = Arr[m + 1 + j];
    }

    int i = 0;
    int j = 0;
    int k = l;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            Arr[k++] = L[i++];
        } else {
            Arr[k++] = R[j++];
        }
        *total++;
    }

    while (i < n1) {
        Arr[k++] = L[i++];
    }
    while (j < n2) {
        Arr[k++] = R[j++];
    }

    free(L);
    free(R);
}

void mergeSort(int Arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(Arr, l, m);
        mergeSort(Arr, m + 1, r);
        merge(Arr, l, m, r);
    }
}

void mergeSort2(int Arr[], int l, int r, int* total) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort2(Arr, l, m, total);
        mergeSort2(Arr, m + 1, r, total);
        merge2(Arr, l, m, r, total);
    }
}

void mergeSortStart(int Arr[], int len) {
    mergeSort(Arr, 0, len - 1);
}

void mergeSortStart2(int Arr[], int len, int* total) {
    mergeSort2(Arr, 0, len - 1, total);
}

int partition(int Arr[], int begin, int end) {
    int pivot = Arr[end];
    int i = begin - 1;

    for (int j = begin; j <= end - 1; j++) {
        if (Arr[j] < pivot) {
            i++;
            swap(&Arr[i], &Arr[j]);
        }
    }
    swap(&Arr[i + 1], &Arr[end]);
    return i + 1;
}

int partition2(int Arr[], int begin, int end, int* total) {
    int pivot = Arr[end];
    int i = begin - 1;

    for (int j = begin; j <= end - 1; j++) {
        if (Arr[j] < pivot) {
            i++;
            swap(&Arr[i], &Arr[j]);
            *total++;
        }
    }
    swap(&Arr[i + 1], &Arr[end]);
    *total++;
    return i + 1;
}

void quickSort(int Arr[], int begin, int end) {
    if (begin < end) {
        int pivot = partition(Arr, begin, end);
        quickSort(Arr, begin, pivot - 1);
        quickSort(Arr, pivot + 1, end);
    }
}

void quickSort2(int Arr[], int begin, int end, int* total) {
    if (begin < end) {
        int pivot = partition2(Arr, begin, end, total);
        quickSort2(Arr, begin, pivot - 1, total);
        quickSort2(Arr, pivot + 1, end, total);
    }
}

void quickSortStart(int Arr[], int len) {
    quickSort(Arr, 0, len - 1);
}

void quickSortStart2(int Arr[], int len, int* total) {
    quickSort2(Arr, 0, len - 1, total);
}