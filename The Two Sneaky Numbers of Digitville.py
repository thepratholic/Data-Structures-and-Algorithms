from typing import List
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        frequency = {}
        result = []

        # Traverse the array and count occurrences of each number
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Find the two numbers that appear twice
        for num, count in frequency.items():
            if count == 2:
                result.append(num)

        return result