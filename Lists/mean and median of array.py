
#User function Template for python3

class Solution:
    ##Complete the below codes
    #Function to find median of the array elements.
    def median(self,A,N):
        
        A.sort()
        
        ##Your code here
        #If median is fraction then convert the median to integer and return
        n = len(A)
        if n % 2 == 1:
            median = int(A[n//2])
        else:
            median = int(A[n//2 - 1] + A[n//2]) // 2
        return median
     
    #Function to find mean of the array elements.   
    def mean(self,A,N):
        ##Your code here
        return int(sum(A) / N)