#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        res, maxEnding = arr[0], arr[0]
        
        n = len(arr)
        for i in range(1, n):
            maxEnding = max(maxEnding + arr[i], arr[i])
            res = max(res, maxEnding)
            
        return res