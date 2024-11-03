def leftIndex (arr, n, X):

        low, high = 0, n-1
        while low<=high:
            mid = (low + high) // 2

            if arr[mid] < X: low = mid + 1
            elif arr[mid] > X: high = mid - 1
            else:
                if mid == 0 or arr[mid] != arr[mid-1]:
                    return mid
                else:
                    high = mid - 1

        return -1

def lastOccurence(arr, n, x):
    low, high = 0, n-1
    while low <= high:
        mid = (low + high) >> 1

        if arr[mid] < x: low = mid + 1
        if arr[mid] > x: high = mid - 1
        else:
            if mid == n-1 or arr[mid] != arr[mid + 1]:
                return mid
            else: low = mid + 1

    return -1

def countOccurences(arr, n, x):
    first = leftIndex(arr, n, x)
    last = lastOccurence(arr, n, x)

    return last - first + 1

print(countOccurences([10, 10, 10, 10], 4, 10))