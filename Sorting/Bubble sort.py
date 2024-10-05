class Solution:
    
    def bubble_sort(self, arr, n):
        
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr
    
s = Solution()
print(s.bubble_sort([9, 1, 4, 7], 4))