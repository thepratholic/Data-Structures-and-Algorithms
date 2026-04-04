from collections import deque

class Solution:
    def isValid(self, i, j, n, m):
        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False
        return True

    def shortestPath(self, grid, source, destination):
        if source == destination:
            return 0

        q = deque()
        n, m = len(grid), len(grid[0])

        q.append((0, source[0], source[1]))
        distance = [[float("inf")] * m for _ in range(n)]

        distance[source[0]][source[1]] = 0

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        while q:
            current_dist, row, col = q.popleft()

            if (row, col) == destination:
                return current_dist

            for i in range(4):
                nrow = row + delRow[i]
                ncol = col + delCol[i]

                if (self.isValid(nrow, ncol, n, m) and 
                    grid[nrow][ncol] == 1 and 
                    current_dist + 1 < distance[nrow][ncol]):

                    distance[nrow][ncol] = current_dist + 1
                    q.append((current_dist + 1, nrow, ncol))

        return -1
