from collections import deque

class Solution:
    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False

        if j < 0 or j >= m:
            return False

        return True

    def bfs(self, row, col, visited, grid):
        visited[row][col] = True
        n, m = len(grid), len(grid[0])

        q = deque()
        q.append((row, col))

        while q:
            cur_row, cur_col = q.popleft()

            for delRow in range(-1, 2):
                for delCol in range(-1, 2):
                    nrow = cur_row + delRow
                    ncol = cur_col + delCol

                    if (self.isValid(nrow, ncol, n, m) and grid[nrow][ncol] == '1' and not visited[nrow][ncol]):
                        q.append((nrow, ncol))
                        visited[nrow][ncol] = True

                        

            
    def numIslands(self, grid):
        n, m = len(grid), len(grid[0])

        visited = [[False] * m for _ in range(n)]

        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    self.bfs(i, j, visited, grid)

        return count