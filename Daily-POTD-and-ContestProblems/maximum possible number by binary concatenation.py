from functools import cmp_to_key
from typing import List
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        binary_strings = [bin(num)[2:] for num in nums]

        def comparator(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1

        sorted_binaries = sorted(binary_strings, key=cmp_to_key(comparator))

        concatenated_binary = ''.join(sorted_binaries)

        return int(concatenated_binary, 2)