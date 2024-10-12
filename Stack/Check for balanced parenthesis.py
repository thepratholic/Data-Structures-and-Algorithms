class Solution:
    def isValid(self, s):
        stack = []
        for i in s:
            if i in ("{", "(", "["):
                stack.append(i)

            else:
                if len(stack) == 0: return False
                elif (i == ")" and stack[-1] == "(") or (i == "}" and stack[-1] == "{") or (i == "]" and stack[-1] == "["):
                    stack.pop()
                else:
                    return False

        if stack: return False
        return True
    
s = Solution()
print(s.isValid("[()"))