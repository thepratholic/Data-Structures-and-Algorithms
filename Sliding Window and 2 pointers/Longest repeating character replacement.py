class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #your code goes here
        n = len(s)
        l, r = 0, 0
        max_len = 0

        maxFreq = 0
        mpp = [0] * 26

        while r < n:
            mpp[ord(s[r]) - ord("A")] += 1

            maxFreq = max(maxFreq, mpp[ord(s[r]) - ord("A")])

            if (r - l + 1) - maxFreq > k:
                mpp[ord(s[l]) - ord("A")] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
