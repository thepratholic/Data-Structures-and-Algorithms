# extension of sliding window technique


def issubsum(arr, sum):
    curr = 0
    s = 0
    for e in range(len(arr)):
        curr += arr[e]
        while curr > sum:
            curr -= arr[s]
            s+=1
        if curr == sum: return True
    return False
arr = [3,2,0,4,7]
sum = 6
print(issubsum(arr,sum))