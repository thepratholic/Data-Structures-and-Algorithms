class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_l = len(s1)
        s1 = sorted(s1)

        for i in range(len(s2)):
            if i + s1_l <= len(s2) and s1 == sorted(s2[i:i+s1_l]):
                return True

        return False
    
s = Solution()
print(s.checkInclusion("ab", "eidbaooo"))