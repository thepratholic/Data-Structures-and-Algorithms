class Solution:

    def helper(self, i, j, path, grid, ans, n):
        if (i == n-1) and (j == n-1):
            ans.append(path)
            return 

        grid[i][j] = 0

        if i-1 >= 0 and grid[i-1][j] == 1 :
            self.helper(i-1, j, path + "U", grid, ans, n)
        
        if j+1 < n and grid[i][j+1] == 1 :
            self.helper(i, j+1, path + "R", grid, ans, n)

        if i+1 < n and grid[i+1][j] == 1:
            self.helper(i+1, j, path + "D", grid, ans, n)
        
        if j-1 >= 0 and grid[i][j-1] == 1:
            self.helper(i, j-1, path + "L", grid, ans, n)
        
        grid[i][j] = 1

    def findPath(self, grid):
        #your code goes here
        n = len(grid)
        ans = []
        if (grid[0][0] == 0) or (grid[n-1][n-1] == 0):
            return ans

        self.helper(0, 0, "", grid, ans, n)
        ans.sort()
        return ans
