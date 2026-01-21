from collections import deque

class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]

    def isValid(self, i, j, n, m):
        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False
        return True

    def nearest(self, grid):
        n, m = len(grid), len(grid[0])

        q = deque()

        visited = [[False] * m for _ in range(n)]
        distance = [[-1] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j, 0)) # row, col, dist
                    visited[i][j] = 0

        while q:
            row, col, dist = q.popleft()

            distance[row][col] = dist
            
            for i in range(4):
                nrow = row + self.delRow[i]
                ncol = col + self.delCol[i]

                if self.isValid(nrow, ncol, n, m) and grid[nrow][ncol] == 0 and not visited[nrow][ncol]:
                    visited[nrow][ncol] = True
                    q.append((nrow, ncol, dist + 1))

        return distance