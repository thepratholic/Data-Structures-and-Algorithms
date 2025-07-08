from collections import defaultdict
class Solution:
    def totalFruits(self, fruits):
        #your code goes here
        n = len(fruits)
        l, r = 0, 0
        max_len = 0
        mpp = defaultdict(int)

        while r < n:
            mpp[fruits[r]] += 1

            if len(mpp) > 2:
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]] == 0:
                    del mpp[fruits[l]]

                l += 1

            if len(mpp) <= 2:
                max_len = max(max_len, r - l + 1)
            r += 1

        return max_len