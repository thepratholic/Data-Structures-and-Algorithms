class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #your code goes here
        if dividend == divisor:
            return 1

        isPositive = True
        if dividend < 0 and divisor > 0:
            isPositive = False
        
        if dividend >= 0 and divisor < 0:
            isPositive = False

        n = abs(dividend)
        d = abs(divisor)

        ans = 0
        while n >= d:
            power = 0

            while n >= (d * (1 << power + 1)):
                power += 1
            ans += (1 << power)
            n -= (d * (1 << power))

        if ans >= 2**31 - 1 and isPositive:
            return 2**31 - 1

        if ans >= 2**31 - 1 and not isPositive:
            return -2**31

        return ans if isPositive else -1 * ans

