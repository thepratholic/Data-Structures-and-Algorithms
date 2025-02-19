class Solution:
    def findKRotation(self, arr):
        n = len(arr)
        ans = float("inf")
        smallest_index = -1

        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2

            # left half is sorted
            if arr[low] <= arr[mid]:
                if arr[low] < ans:
                    smallest_index = low
                    ans = arr[low]

                low = mid + 1

            # right half is sorted
            else:
                if arr[mid] < ans:
                    smallest_index = mid
                    ans = arr[mid]
                high = mid - 1

        return smallest_index