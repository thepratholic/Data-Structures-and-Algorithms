class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]

    def isValid(self, i, j, n, m):
        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False
        return True

    def dfs(self, row, col, visited, mat):
        visited[row][col] = True
        n, m = len(mat), len(mat[0])
        for i in range(4):
            nrow = row + self.delRow[i]
            ncol = col + self.delCol[i]

            if self.isValid(nrow, ncol, n, m) and mat[nrow][ncol] == 'O' and not visited[nrow][ncol]:
                self.dfs(nrow, ncol, visited, mat)
                
    def fill(self, mat):
        n, m = len(mat), len(mat[0])

        visited = [[False] * m for _ in range(n)]

        for j in range(m):
            if not visited[0][j] and mat[0][j] == 'O':
                self.dfs(0, j, visited, mat)

            if not visited[n - 1][j] and mat[n - 1][j] == 'O':
                self.dfs(n - 1, j, visited, mat)

        
        for i in range(n):
            if not visited[i][0] and mat[i][0] == 'O':
                self.dfs(i, 0, visited, mat)

            if not visited[i][m - 1] and mat[i][m - 1] == 'O':
                self.dfs(i, m - 1, visited, mat)

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O' and not visited[i][j]:
                    mat[i][j] = 'X'

        return mat