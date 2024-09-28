from typing import List
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        for i in encoded:
            decoded.append(decoded[-1] ^ i)
        return decoded
    
s = Solution()
print(s.decode([1, 2, 3], 1))