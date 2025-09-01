class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        n = len(nums)

        stack = []
        for i in range(n):
            while stack and k > 0 and stack[-1] > nums[i]:
                stack.pop()
                k -= 1

            stack.append(nums[i])
        
        while stack and k > 0:
            stack.pop()
            k -= 1

        if not stack:
            return "0"

        result = ""
        while stack:
            result += stack.pop()

        result = result.rstrip("0")
        result = result[::-1]

        if not result:
            return "0"

        return result
