from collections import defaultdict
from typing import List
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []
        
        # Frequency map for the current window
        freq_map = defaultdict(int)
        
        # Calculate frequency for the first window
        for i in range(k):
            freq_map[nums[i]] += 1
        
        # Helper function to calculate x-sum
        def calculate_x_sum(freq_map, x):
            freq_list = sorted(freq_map.items(), key=lambda item: (-item[1], -item[0])) # Sort by freq, then value
            total_sum = 0
            count = 0
            
            for value, freq in freq_list:
                if count < x:
                    total_sum += value * freq
                    count += 1
                else:
                    break
            
            return total_sum
        
        # Add x-sum for the first window
        answer.append(calculate_x_sum(freq_map, x))
        
        # Slide the window
        for i in range(1, n - k + 1):
            # Remove the element going out of the window
            freq_map[nums[i - 1]] -= 1
            if freq_map[nums[i - 1]] == 0:
                del freq_map[nums[i - 1]]
            
            # Add the new element coming into the window
            freq_map[nums[i + k - 1]] += 1
            
            # Calculate x-sum for the current window
            answer.append(calculate_x_sum(freq_map, x))
        
        return answer