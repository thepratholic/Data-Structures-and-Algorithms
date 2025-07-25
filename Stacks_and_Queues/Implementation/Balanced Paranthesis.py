class Solution:
    def matched(self, open, close):
        if (open == "(" and close == ")") or (open == "{" and close == "}") or (open == "[" and close == "]"):
            return True

        return False

    def isValid(self, str: str) -> bool:
        stack = []

        for i in str:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            
            else:
                if len(stack) == 0:
                    return False

                ch = stack[-1]
                stack.pop()

                if not self.matched(ch, i):
                    return False

        return len(stack) == 0