class Solution(object):
    def isValid(self, s):
        #your code goes here
        minOpen, maxOpen = 0, 0
        
        for char in s:
            if char == "(":
                minOpen += 1
                maxOpen += 1
            
            elif char == ")":
                minOpen -= 1
                maxOpen -= 1

            else:
                minOpen -= 1
                maxOpen += 1

            if minOpen < 0:
                minOpen = 0
            if maxOpen < 0:
                return False

        return minOpen == 0