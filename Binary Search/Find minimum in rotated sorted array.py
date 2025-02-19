class Solution:
    def findMin(self, arr):
        n = len(arr)
        ans = float("inf")

        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2

            # left half is sorted
            if arr[low] <= arr[mid]:
                ans = min(ans, arr[low])
                low = mid + 1

            # right half is sorted
            else:
                ans = min(ans, arr[mid])
                high = mid - 1

        return ans