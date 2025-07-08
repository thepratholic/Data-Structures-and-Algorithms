class Solution:
    def longestNonRepeatingSubstring(self, s):
        #your code goes here
        n = len(s)
        hash_set = [-1] * 256
        l, r = 0, 0
        max_len = 0

        while r < n:

            if hash_set[ord(s[r])] != -1:
                if hash_set[ord(s[r])] >= l:
                    l = hash_set[ord(s[r])] + 1
                
            max_len = max(max_len, r - l + 1)
            hash_set[ord(s[r])] = r
            r += 1

        return max_len