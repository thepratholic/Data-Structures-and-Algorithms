class Solution:
    def maxElement(self, mat, col):
        n, m = len(mat), len(mat[0])
        max_val, index = -1, -1
        for i in range(n):
            if mat[i][col] > max_val:
                max_val = mat[i][col]
                index = i 
        return index

    def findPeakGrid(self, mat):
        n, m = len(mat), len(mat[0])

        low, high = 0, m - 1
        while low <= high:
            mid = (low + high) // 2

            row = self.maxElement(mat, mid)

            left = mat[row][mid-1] if mid-1 >= 0 else float("-inf")
            right = mat[row][mid + 1] if mid + 1 < m else float("-inf")

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]
            
            elif mat[row][mid] < left:
                high = mid - 1

            else:
                low = mid + 1

        return [-1, -1]