class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        first_occurrence = {0: -1} 
        max_len = 0
        
        for i, char in enumerate(s):
            if char == 'a':
                mask ^= 1
            elif char == 'e':
                mask ^= 2
            elif char == 'i':
                mask ^= 4
            elif char == 'o':
                mask ^= 8
            elif char == 'u':
                mask ^= 16

            if mask in first_occurrence:
                max_len = max(max_len, i - first_occurrence[mask])
            else:
                first_occurrence[mask] = i  
        
        return max_len