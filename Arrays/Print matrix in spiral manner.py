class Solution:
    def spiralOrder(self, mat):
        n, m = len(mat), len(mat[0])
        ans = []
        left, right, top, bottom = 0, m - 1, 0, n - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                ans.append(mat[top][i])
            top += 1

            for i in range(top, bottom + 1):
                ans.append(mat[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(mat[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(mat[i][left])
                left += 1

        return ans
        