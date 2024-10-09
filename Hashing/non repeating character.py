class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        #code here
        d = {}
        
        for i in s:
            if i not in d: d[i] = 1
            else: d[i] += 1
        
        
        for i in s:
            if d[i] == 1: return i
            
        return "$"