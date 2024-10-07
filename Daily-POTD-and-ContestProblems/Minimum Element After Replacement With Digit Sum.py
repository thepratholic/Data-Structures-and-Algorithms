from typing import List
class Solution:
    def digit_sum(self,n):
        return sum(int(digit) for digit in str(n))

    def minElement(self, nums: List[int]) -> int:
        new_nums = [self.digit_sum(num) for num in nums]
        return min(new_nums)