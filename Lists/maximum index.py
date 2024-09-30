#User function Template for python3
class Solution:
    def maxIndexDiff(self, arr):
        # code here
        n = len(arr)
        left_min = [0] * n
        right_max = [0] * n
        
        left_min[0] = arr[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i-1], arr[i])
            
        right_max[n-1] = arr[n-1]
        
        for j in range(n-2, -1, -1):
            right_max[j] = max(arr[j], right_max[j+1])
        
        i,j = 0,0
        max_diff = -1
        while i < n and j < n:
            if left_min[i] <= right_max[j]:
                max_diff = max(max_diff, j - i)
                j += 1
            else:
                i += 1

        return max_diff