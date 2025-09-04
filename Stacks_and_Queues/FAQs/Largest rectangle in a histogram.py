class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        n = len(heights)
        max_area = float('-inf')

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
