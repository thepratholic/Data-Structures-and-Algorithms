class Solution:
    def maxScore(self, cardScore, k):
        #your code goes here
        n = len(cardScore)
        left_sum, right_sum = 0, 0
        max_score = 0
        for i in range(k):
            left_sum += cardScore[i]

        max_score = max(max_score, left_sum)

        right_index = n - 1

        for i in range(k-1, -1, -1):
            left_sum -= cardScore[i]
            right_sum += cardScore[right_index]
            right_index -= 1
            max_score = max(max_score, left_sum + right_sum)

        return max_score