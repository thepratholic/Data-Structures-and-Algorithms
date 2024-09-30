#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def maxSubarraySum(arr):
    n = len(arr)
    maxEnding = arr[0]
    res = arr[0]
    for i in range(1, n):
        maxEnding = max(maxEnding + arr[i], arr[i])
        res = max(res, maxEnding)
    return res
    
def circularSubarraySum(arr):
    ##Your code here
    
    maxNormal = maxSubarraySum(arr)
    if maxNormal < 0: 
        return maxNormal
    
    n = len(arr)
    arr_sum = 0
    for i in range(0, n):
        arr_sum += arr[i]
        arr[i] *= -1
    
    max_circular = arr_sum + maxSubarraySum(arr)
    return max(max_circular, maxNormal)