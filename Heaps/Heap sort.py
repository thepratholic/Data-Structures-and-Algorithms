class Heap:
    def buildHeap(self, arr):
        n = len(arr)
        for i in range(n - 2 // 2, -1, -1):
            self.maxHeapify(arr, i, n)

    def maxHeapify(self, arr, i, n):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.maxHeapify(arr, largest, n-1)

    def heapSort(self, arr):
        n = len(arr)
        self.buildHeap(arr)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.maxHeapify(arr, 0, i)


h = Heap()
arr = [3, 9, 11, 2]
h.heapSort(arr)
print(arr)