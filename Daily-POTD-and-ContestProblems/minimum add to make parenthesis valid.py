class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        #we have to solve this problem in minimized space complexity
        openBrackets, mini_adds = 0, 0
        for ch in s:
            if ch == "(":
                openBrackets += 1
            else:
                if openBrackets > 0:
                    openBrackets -= 1
                else:
                    mini_adds += 1
        return mini_adds + openBrackets