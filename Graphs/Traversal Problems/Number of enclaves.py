from collections import deque

class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]

    def isValid(self, i, j, n, m):
        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False
        return True

    def numberOfEnclaves(self, grid):
        q = deque()
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    if grid[i][j] == 1:
                        q.append((i, j))
                        visited[i][j] = True

        
        while q:
            row, col = q.popleft()

            for i in range(4):
                nRow = row + self.delRow[i]
                nCol = col + self.delCol[i]

                if self.isValid(nRow, nCol, n, m) and grid[nRow][nCol] == 1 and visited[nRow][nCol] == False:
                    visited[nRow][nCol] = True
                    q.append((nRow, nCol))

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    ans += 1

        return ans