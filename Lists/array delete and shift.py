#User function Template for python3

def deleteFromArray(arr,n,idx):
    #code here
    
    # del arr[idx]
    
    for i in range(idx, n-1):
        arr[i] = arr[i+1]
        
    arr[-1] = 0
    return arr