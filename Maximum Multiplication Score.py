from typing import List

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [-float('inf')] * 5
        dp[0] = 0  # Base case: No elements picked, score is 0
        
        # Iterate through elements of b
        for num in b:
            # Iterate backward through a (4 down to 1) to update the DP table
            for i in range(4, 0, -1):
                dp[i] = max(dp[i], dp[i-1] + a[i-1] * num)
        
        return dp[4]