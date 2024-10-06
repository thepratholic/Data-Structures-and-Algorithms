class Solution:
    cnt = 0
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
                self.cnt += (mid - low - i + 1)
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
    def inversionCount(self, arr):
        # Your Code Here
        n = len(arr)
        self.mergeSort(arr, 0, n-1)
        return self.cnt
    
s = Solution()
print(s.inversionCount([8,4,2,1]))