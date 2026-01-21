class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]

    def isValid(self, i, j, n, m):
        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False
        return True

    def dfs(self, row, col, visited, grid, base_row, base_col, path):
        n, m = len(grid), len(grid[0])
        visited[row][col] = True
        path.append((row - base_row, col - base_col))

        for i in range(4):
            nrow = row + self.delRow[i]
            ncol = col + self.delCol[i]

            if(self.isValid(nrow, ncol, n, m) and grid[nrow][ncol] == 1
                and not visited[nrow][ncol]):
                self.dfs(nrow, ncol, visited, grid, base_row, base_col, path)

            
    def countDistinctIslands(self, grid):
        n, m = len(grid), len(grid[0])
        st = set()
        visited = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    v = []
                    self.dfs(i, j, visited, grid, i, j, v)
                    st.add(tuple(v))

        return len(st)