def isPair(arr, n, x, si):
    i, j = si, n-1
    while i <= j:
        if arr[i] + arr[j] == x:
            return True
        elif arr[i] + arr[j] > x:
            j -= 1
        else: i+=1

    return False

def triplet(arr, n, x):
    for i in range(n-2):
        if(isPair(arr, n, x - arr[i], i+1)):
            return True
    return False

print(triplet([1, 3, 8, 10, 15], 5, 27))