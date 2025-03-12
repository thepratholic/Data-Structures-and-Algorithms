class Solution:
    def isSafe(self, board, row, col):
        n = len(board)
        
        # Check this column on the upper side
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check upper diagonal on the right side
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False
        
        return True

    def helper(self, row, board, ans):
        n = len(board)
        if row == n:
            ans.append(list(board))
            return

        for col in range(n):
            if self.isSafe(board, row, col):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]  # Place queen
                self.helper(row + 1, board, ans)  # Move to the next row
                board[row] = board[row][:col] + '.' + board[row][col+1:]  # Backtrack by removing queen

    def solveNQueens(self, n):
        board = ["." * n for _ in range(n)]
        ans = []
        self.helper(0, board, ans)
        return ans
