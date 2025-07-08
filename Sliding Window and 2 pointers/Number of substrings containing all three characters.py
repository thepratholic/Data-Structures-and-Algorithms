class Solution:    
    def numberOfSubstrings(self, s: str) -> int:
        #your code goes here
        n = len(s)

        last_seen = [-1] * 3
        count = 0

        for i in range(n):
            last_seen[ord(s[i]) - ord("a")] = i 

            if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
                count += (1 + min(last_seen[0], last_seen[1], last_seen[2]))

        return count