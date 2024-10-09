class Solution:
    def countVowels(self,s):
        #code here
        cnt = 0
        # s = set(s)
        for ch in s:
            if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
                cnt += 1
        return cnt 