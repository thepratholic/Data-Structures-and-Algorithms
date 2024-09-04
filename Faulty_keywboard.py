class Solution:
    def finalString(self, s: str) -> str:
        strr = ""
        revstr = ""
        for c in s:
            if c != "i":
                strr += c
                revstr += c
            else:
                strr, revstr = revstr, strr
        return strr
    
s = Solution()
print(s.finalString("string"))