class Solution:
    def find_floor(self, arr, n, x):

        low, high, floor_index = 0, n-1, -1
        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == x: return mid
            elif arr[mid] < x:
                floor_index == mid
                low = mid + 1
            else:
                high = mid - 1
        return floor_index

s = Solution()
print(s.find_floor([1,2,8,10,11,12,19], 7, 0))