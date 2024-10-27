class Solution:
    def maxScore(self, cards, k):
        n, lSum, rSum, maxSum = len(cards), 0, 0, 0
        for i in range(k):
            lSum += cards[i]
            maxSum = max(maxSum, lSum)

        rIndex = n- 1
        for j in range(k-1, -1, -1):
            lSum -= cards[j]
            rSum += cards[rIndex]
            rIndex -= 1
            maxSum = max(maxSum, lSum + rSum)

        return maxSum

s = Solution()
print(s.maxScore([1,2,3,4,5,6,1], 3))