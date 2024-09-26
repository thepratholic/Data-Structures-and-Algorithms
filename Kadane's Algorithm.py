class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        cs = maxs = arr[0]
        for i in arr[1:]:
            cs = max(i, i+cs)
            maxs = max(maxs, cs)
            
        return maxs
