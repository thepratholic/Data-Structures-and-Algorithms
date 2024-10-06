class Solution:
    
    def partition(self, arr, low, high):
        i = j = low
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
    
s = Solution()
print(s.partition([10, 7, 8, 9, 1, 5], 0, 5))