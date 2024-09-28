from typing import List

class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)

        total_height = 0
        current_height = float('inf') 

        for height in maximumHeight:
            if current_height > height:
                current_height = height
            if current_height <= 0:
                return -1
            total_height += current_height
            current_height -= 1 

        return total_height