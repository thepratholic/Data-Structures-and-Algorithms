class Solution:
    def nextGreaterElements(self, arr):
        n = len(arr)
        nge = [-1] * n 
        stack = []

        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= arr[i % n]:
                stack.pop()

            if i < n:
                nge[i] = -1 if not stack else stack[-1]

            stack.append(arr[i%n])

        return nge