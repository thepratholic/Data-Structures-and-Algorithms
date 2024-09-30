class Solution:
    # Complete this function
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,arr):
        # Your code here
        n = len(arr)
        leftSum = 0
        rightSum = sum(arr)
        
        for i in range(n):
            rightSum -= arr[i]
            if leftSum == rightSum:
                return i+1
                
            leftSum += arr[i]
            
        return -1