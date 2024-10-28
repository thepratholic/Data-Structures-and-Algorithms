class Solution:
    def numberOfSubstrings(self, s):
        lastSeen = [-1] * 3
        n = len(s)
        cnt = 0
        for i in range(n):
            lastSeen[ord(s[i]) - ord('a')] = i
            cnt += (1 + min(lastSeen[0], lastSeen[1], lastSeen[2]))
        return cnt

s= Solution()
print(s.numberOfSubstrings("abcabc"))