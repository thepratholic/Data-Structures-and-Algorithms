class Solution:
    def lomutoPartition(self, arr, low, high):
        i = j = low
        pivot = arr[high]
        i = low-1
        for j in range(low, high):
            if arr[j] <= pivot:
                i+=1
                arr[j], arr[i] = arr[i], arr[j]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    def QuickSort(self, arr, low, high):
        if low < high:
            p = self.lomutoPartition(arr, low, high)
            self.QuickSort(arr, low, p-1)
            self.QuickSort(arr, p+1, high)
        return arr

s = Solution()
print(s.QuickSort([4, 2, 9, 6], 0, 3))