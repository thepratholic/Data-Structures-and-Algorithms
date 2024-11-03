def isPair(arr, n, x):
    i, j = 0, n-1
    while i <= j:
        if arr[i] + arr[j] == x:
            return True
        elif arr[i] + arr[j] > x:
            j -= 1
        else: i+=1

    return False

print(isPair([2, 5, 8, 12, 30], 5, 17))