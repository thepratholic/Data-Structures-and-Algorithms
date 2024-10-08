class Solution:
    def countFreq(self, arr, n):
        d = {}

        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for i in range(n):
            if (d[arr[i]] != -1):
                print(arr[i], d[arr[i]])
            d[arr[i]] = -1

s = Solution()
s.countFreq([10, 80, 30, 10, 30], 5)