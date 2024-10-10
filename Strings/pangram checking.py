class Solution:
    def isPangram(self, s):
        s = s.lower()

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] = 1

        for x in count:
            if x == 0: return False

        return True
s = Solution()
print(s.isPangram("HeavyDuty"))