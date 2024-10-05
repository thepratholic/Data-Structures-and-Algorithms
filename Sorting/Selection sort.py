class Solution:
    def selection_sort(self, arr, n):
        
        for i in range(n-1):
            mini = i
            for j in range(i+1, n):
                if arr[j] < arr[mini]:
                    mini = j

            arr[mini], arr[i] = arr[i], arr[mini]

        return arr
    
s = Solution()
print(s.selection_sort([4, 1, 7, 0], 4))