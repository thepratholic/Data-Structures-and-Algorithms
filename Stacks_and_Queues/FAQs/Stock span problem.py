class Solution:
    def findPGE(self, arr):
        n = len(arr)
        stack = []
        pge = [-1] * n 

        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            pge[i] = stack[-1] if stack else -1 
            stack.append(i)
        return pge

    def stockSpan(self, arr, n):
        ans = [0] * n 

        pge = self.findPGE(arr)

        for i in range(n):
            ans[i] = i - pge[i]

        return ans