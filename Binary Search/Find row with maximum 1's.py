class Solution:
    def lowerBound(self, sorted_array, target):
        n = len(sorted_array)
        low, high = 0, n - 1
        ans = n 
        while low <= high:
            mid = (low + high) // 2

            if sorted_array[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def rowWithMax1s(self, mat):
        max_count = 0
        index = -1
        n, m = len(mat), len(mat[0])

        for i in range(n):
            cnt_ones = m - self.lowerBound(mat[i], 1)
            if cnt_ones > max_count:
                max_count = cnt_ones
                index = i 

        return index

       