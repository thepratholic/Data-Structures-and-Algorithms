class Solution:
    def largestHistogram(self, heights):
        n = len(heights)
        stack = []
        max_area = 0

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                nse = i 
                element = stack.pop()
                pse = stack[-1] if stack else -1
                max_area = max(max_area, heights[element] * (nse - pse - 1))
            stack.append(i)

        while stack:
            nse = n  
            element = stack.pop()
            pse = stack[-1] if stack else -1
            max_area = max(max_area, heights[element] * (nse - pse - 1))
        return max_area

    def maximalAreaOfSubMatrixOfAll1(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        pSum = [[0] * m for i in range(n)]

        for j in range(m):
            sum = 0
            for i in range(n):
                sum += matrix[i][j]
                if matrix[i][j] == 0:
                    sum = 0
                pSum[i][j] = sum

        max_area = 0

        for i in range(n):
            max_area = max(max_area, self.largestHistogram(pSum[i]))

        return max_area
