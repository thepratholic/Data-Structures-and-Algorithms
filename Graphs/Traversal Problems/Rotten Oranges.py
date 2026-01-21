from collections import deque

class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]

    def isValid(self, i, j, n, m):
        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False
        return True


    def orangesRotting(self, grid):
        q = deque()
        n, m = len(grid), len(grid[0])

        visited = [[False] * m for _ in range(n)]

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited[i][j] = True

        
        while q:
            row, col, time = q.popleft()
            ans = max(ans, time)

            for i in range(4):
                nrow = row + self.delRow[i]
                ncol = col + self.delCol[i]

                if self.isValid(nrow, ncol, n, m) and grid[nrow][ncol] == 1 and not visited[nrow][ncol]:
                    visited[nrow][ncol] = True
                    q.append((nrow, ncol, time + 1))

        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    return -1

        return ans