#User function Template for python3

class Solution:
    ##Complete this function
    #Function to check if array is sorted and rotated.
    def checkRotatedAndSorted(self,arr,n):
        #code here    
        
        cnt_inc = 0
        cnt_dec = 0
        for i in range(n-1):
            if arr[i] < arr[i+1]:
                cnt_inc += 1
            else: cnt_dec += 1
            
        if cnt_inc == 1 or cnt_dec == 1:
            if arr[n-1] < arr[0]:
                cnt_inc += 1
            else: cnt_dec += 1
            
            if cnt_inc == 1 or cnt_dec == 1:
                return True
        return False