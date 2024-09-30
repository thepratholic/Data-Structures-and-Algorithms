#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        maxi = max(arr)
        if maxi < 0:
            return 1
            
        else:
            for i in range(1, maxi+1):
                if i not in arr:
                    return i
                    
            else:
                return maxi + 1