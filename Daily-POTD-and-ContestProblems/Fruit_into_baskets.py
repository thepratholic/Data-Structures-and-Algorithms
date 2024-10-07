class Solution:
    def totalFruits(self,arr):
        l, r, maxlen, d = 0,0,0, {}
        n = len(arr)
        while r < n:
            if arr[r] in d:
                d[arr[r]] += 1
            else:
                d[arr[r]] = 1
            if len(d) > 2:
                d[arr[l]] -= 1
                if d[arr[l]] == 0:
                    del d[arr[l]]
                l+=1
            if len(d) <= 2:
                maxlen = max(maxlen, r-l+1)
            r+=1
        return maxlen

s=Solution()
print(s.totalFruits([3, 1, 2, 2, 2, 2]))