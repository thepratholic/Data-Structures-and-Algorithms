class Solution:
    def findNSE(self, arr):
        n = len(arr)
        nse = [-1] * n 
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else n 
            stack.append(i)
        return nse

    def findNGE(self, arr):
        n = len(arr)
        nge = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            nge[i] = stack[-1] if stack else n 
            stack.append(i)
        return nge

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

    def findPGEE(self, arr):
        n = len(arr)
        stack = []
        pge = [-1] * n 
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            pge[i] = stack[-1] if stack else -1
            stack.append(i)
        return pge

    def sumSubarrayMins(self, arr):
        nse = self.findNSE(arr)
        pse = self.findPSEE(arr)

        total = 0
        n = len(arr)
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i 

            total = total + (left * right * arr[i])

        return total

    def sumSubarrayMaxs(self, arr):
        nge = self.findNGE(arr)
        pge = self.findPGEE(arr)
        total = 0
        n = len(arr)
        for i in range(n):
            left = i - pge[i]
            right = nge[i] - i 

            total = total + (left * right * arr[i])

        return total

    def subArrayRanges(self, nums):
        return self.sumSubarrayMaxs(nums) - self.sumSubarrayMins(nums)