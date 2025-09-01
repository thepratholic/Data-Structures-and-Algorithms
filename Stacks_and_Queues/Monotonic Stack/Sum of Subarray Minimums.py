class Solution:
    def findNSE(self, arr):
        n = len(arr)
        nse = [-1] * n 
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            nse[i] = stack[-1] if stack else n 
            stack.append(i)
        return nse

    def findPSEE(self, arr):
        n = len(arr)
        pse = [-1] * n 
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            pse[i] = stack[-1] if stack else -1
            stack.append(i)
        return pse

    def sumSubarrayMins(self, arr):
        n = len(arr)
        nse = self.findNSE(arr)
        pse = self.findPSEE(arr)

        total = 0
        MOD = int(1e9 + 7)

        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i 

            subarrays = left * right

            val = (subarrays * arr[i]) % MOD
            total = (total + val) % MOD

        return total