#User function template for Python

class Solution:
    #Function to find the days of buying and selling stock for max profit.
    def stockBuySell(self, arr, n):
        #code here
        profit = 0
        ans = []
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                ans.append([i-1, i])
        return ans
            