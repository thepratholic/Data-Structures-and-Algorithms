class Solution:
    def leftIndex (self, N, arr, X):

        low, high = 0, N-1
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