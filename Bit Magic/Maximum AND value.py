class Solution:

    def checkBit(self, pattern, arr, n):
        count = 0
        for i in range(n):
            if pattern & arr[i] == pattern:
                count += 1

        return count

    def maxAND(self, arr,n):
        #Your code here
        res = 0
        count = 0

        for i in range(16, -1, -1):
            count = self.checkBit((res | (1<<i)), arr, n)

            if count >= 2:
                res |= (1<<i)
        return res