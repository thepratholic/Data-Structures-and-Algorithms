class Solution:
    
    #Complete this code
    #Function to return the count of non-repeated elements in the array.
    def countNonRepeated(self,arr,n):
        #Your code here
        d = {}
        
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        cnt = 0
        for i in d:
            if d[i] == 1:
                cnt += 1
                
        return cnt