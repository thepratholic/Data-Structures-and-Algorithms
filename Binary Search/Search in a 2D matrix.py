class Solution:
    def searchMatrix(self, mat, target):
        n, m = len(mat), len(mat[0])

        low, high = 0, (n * m) - 1
        while low <= high:
            mid = (low + high) // 2

            row, col = mid // m, mid % m 

            if mat[row][col] == target:
                return True

            elif mat[row][col] < target:
                low = mid + 1

            else:
                high = mid - 1

        return False