#User function Template for python3

class Solution:
    def immediateSmaller(self,arr,n,x):
        #return required ans
        
        #code here
        mini = -1
        for i in arr:
            if i < x:
                if mini == -1 or (x-i) < (x - mini):
                    mini = i

        return mini
