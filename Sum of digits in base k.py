class Solution:
    def sumBase(self, n: int, k: int) -> int:
        sum = 0
        while n > 0:
            sum += n % k
            n = math.floor(n / k)
        return sum
