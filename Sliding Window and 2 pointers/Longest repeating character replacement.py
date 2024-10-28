class Solution:
    def characterReplacement(self, s, k):
        n, l, r, maxLen, maxF, hash = len(s), 0, 0, 0, 0, [0] * 26

        while r < n:
            hash[ord(s[r]) - ord('A')] += 1
            maxF = max(maxF, hash[ord(s[r]) - ord('A')])

            if (r - l + 1) - maxF > k:
                hash[ord(s[l]) - ord('A')] -= 1
                maxF = 0
                l+=1

            if (r - l + 1) - maxF <= k:
                maxLen = max(maxLen, r - l + 1)
            r+=1

        return maxLen

s = Solution()
print(s.characterReplacement("ABAB", 2))