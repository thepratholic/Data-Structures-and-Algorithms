import heapq

class Solution:
    def isValid(self, i, j, n, m):
        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False
        return True

    def MinimumEffort(self, heights):
        pq = []

        n, m = len(heights), len(heights[0])

        distance = [[float("inf")] * m for _ in range(n)]
        distance[0][0] = 0

        heapq.heappush(pq, (0, 0, 0)) # diff, row, col 

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        while pq:
            current_diff, row, col = heapq.heappop(pq)

            if row == n - 1 and col == m - 1:
                return current_diff

            for i in range(4):
                nrow = row + delRow[i]
                ncol = col + delCol[i]

                if (self.isValid(nrow, ncol, n, m)):
                    new_diff = abs(heights[row][col] - heights[nrow][ncol])

                    if max(new_diff, current_diff) < distance[nrow][ncol]:
                        distance[nrow][ncol] = max(new_diff, current_diff)
                        heapq.heappush(pq, (distance[nrow][ncol], nrow, ncol))


        return 0   
