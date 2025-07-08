class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #your code goes here
        n, m = len(s), len(t)
        mpp = [0] * 256
        count, sIndex = 0, -1
        min_len = float("inf")
        l, r = 0, 0

        for i in range(m):
            mpp[ord(t[i])] += 1

        while r < n:
            if mpp[ord(s[r])] > 0:
                count += 1

            mpp[ord(s[r])] -= 1

            while count == m:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    sIndex = l 

                mpp[ord(s[l])] += 1
                if mpp[ord(s[l])] > 0:
                    count -= 1

                l += 1

            r += 1

        return "" if sIndex == -1 else s[sIndex:sIndex + min_len]