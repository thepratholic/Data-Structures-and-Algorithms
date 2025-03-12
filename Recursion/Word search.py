class Solution:
    def helper(self, board, word, i, j, n, m, ind):
        if ind == n:
            return True

        if i < 0 or j < 0 or i >= n or j >= m or word[ind] != board[i][j] or board[i][j] == ' ':
            return False

        board[i][j] = ' '

        ans = (self.helper(board, word, i+1, j, n, m, ind+1) or
               self.helper(board, word, i-1, j, n, m, ind+1) or
               self.helper(board, word, i, j-1, n, m, ind+1) or
               self.helper(board, word, i, j+1, n, m, ind+1))

        return ans

    def exist(self, board, word):
        #your code goes here
        n, m = len(board), len(board[0])
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if self.helper(board, word, i, j, n, m, 0):
                        return True

        return False
