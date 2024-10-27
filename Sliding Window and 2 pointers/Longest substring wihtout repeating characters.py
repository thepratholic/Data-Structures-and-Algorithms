class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = [-1] * 256
        n, l, r, maxLen = len(s), 0, 0, 0
        while r < n:
            if hash[ord(s[r])] != -1:
                l = max(l, hash[ord(s[r])] + 1)
            hash[ord(s[r])] = r
            maxLen = max(maxLen, r - l + 1)
            r+=1
        return maxLen