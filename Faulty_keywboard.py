class Solution:
    def finalString(self, s: str) -> str:
        strr = ""
        revstr = ""
        for c in s:
            if c != "i":
                strr = strr + c
                revstr = c + revstr
            else:
                strr, revstr = revstr, strr
        return strr
    
s = Solution()
print(s.finalString("string"))
