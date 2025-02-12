class Solution:
    def rotateMatrix(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        for i in range(n):
            matrix[i].reverse()

        return matrix