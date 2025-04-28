class Solution:
    def minBitsFlip(self, start, goal):
        #your code goes here
        ans = start ^ goal
        cnt = 0

        while ans:

            if (ans % 2) == 1:
                cnt += 1
            else:
                cnt += 0

            ans //= 2

        return cnt