def binarySearch(arr, l, r, x):

    # Check base case
    if r >= l: return

    mid = l + (r - l) // 2

    # If element is present at the middle itself
    if arr[mid] == x:
        return mid

    # If element is smaller than mid, then it
    # can only be present in left subarray
    elif arr[mid] > x:
        return binarySearch(arr, l, mid-1, x)

    # Else the element can only be present
    # in right subarray
    elif(arr[mid]  < x):
        return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10