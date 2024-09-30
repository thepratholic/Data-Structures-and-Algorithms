def getSum(l, r):
    if l == 0: return pSum[r]
    else: return pSum[r] - pSum[l-1]

arr=[2, 8, 3, 9, 6, 5, 4]
n=len(arr)
pSum=[None]*n 
pSum[0]=arr[0]
for i in range(1, n):
    pSum[i]=pSum[i-1]+arr[i]

# pSum = [2, 10, 13, 22, 28, 33, 37]
print(getSum(2, 6))