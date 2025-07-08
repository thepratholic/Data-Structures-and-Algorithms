from collections import defaultdict
class Solution:
    def kDistinctChar(self, s, k):
        #your code goes here
        n = len(s)
        mpp = defaultdict(int)
        max_len = 0
        l, r = 0, 0

        while r < n:
            mpp[s[r]] += 1

            if len(mpp) > k:
                mpp[s[l]] -= 1
                if mpp[s[l]] == 0:
                    del mpp[s[l]]
                l += 1

            if len(mpp) <= k:
                max_len = max(max_len, r - l + 1)

            r += 1
        return max_len