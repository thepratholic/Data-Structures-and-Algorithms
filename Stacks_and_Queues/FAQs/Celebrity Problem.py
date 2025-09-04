class Solution:
    def celebrity(self, M):
        top = 0
        down = len(M) - 1

        while top < down:
            if M[top][down] == 1:
                top += 1
            
            elif M[down][top] == 1:
                down -= 1

            else:
                top += 1
                down -= 1

        if top > down:
            return -1

        for i in range(len(M)):
            if i == top:
                continue

            if M[top][i] == 1 or M[i][top] == 0:
                return -1

        return top