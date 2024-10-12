class Solution:

    def removeConsecutiveDuplicates(self,s):
        # code here
        stack = []
        stack.append(s[0])
        i = 1
        for i in range(len(s)):
            if s[i] != stack[-1]:
                stack.append(s[i])

        return "".join(stack)