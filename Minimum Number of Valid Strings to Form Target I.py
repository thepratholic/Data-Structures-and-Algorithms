from typing import List
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        dp = [float('inf')] * (n + 1) 
        dp[0] = 0  

        for i in range(n):
            if dp[i] == float('inf'):
                continue

            for word in words:
                word_len = len(word)
                for prefix_len in range(1, word_len + 1):
                    if i + prefix_len <= n and target[i:i + prefix_len] == word[:prefix_len]:
                        dp[i + prefix_len] = min(dp[i + prefix_len], dp[i] + 1)

        return dp[n] if dp[n] != float('inf') else -1