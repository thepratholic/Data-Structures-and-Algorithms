class Solution:
    
    def merge(self, arr, low, mid, high):
        left = arr[low:mid+1]
        right = arr[mid+1 : high+1]
        k = low
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                k+=1
                i+=1
            else:
                arr[k] = right[j]
                k+=1
                j+=1

        while i < len(left):
            arr[k] = left[i]
            k+=1
            i+=1
        while j < len(right):
            arr[k] = right[j]
            k+=1
            j+=1

    def mergeSort(self, arr, low, high):
        if high > low:
            mid = (low + high) // 2
            self.mergeSort(arr, low, mid)
            self.mergeSort(arr, mid+1, high)
            self.merge(arr, low, mid, high)
        return arr
    
s = Solution()
print(s.mergeSort([3, 1, 6, 4, 9, 7], 0, 5))