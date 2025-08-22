class Solution:
    def isValidSudoku(self, board):
        row = set()
        col = set()
        squares = [[], [], []]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and board[i][j] not in row:
                    row.add(board[i][j])
                elif board[i][j] in row:
                    return False
                if board[j][i] != '.' and board[j][i] not in col:
                    col.add(board[j][i])
                elif board[j][i] in col:
                    return False
            row = set()
            col = set()
        for step in range(0,9,3):
            for i in range(9):
                squares[0] += board[i][0:3]
                squares[1] += board[i][3:6]
                squares[2] += board[i][6:9]
                if len(squares[0]) == 9:
                    for square in squares:
                        if not self.squareCheck(square):
                            return False
                    squares = [[], [], []]
        return True

    def squareCheck(self, s):
        square = set()
        for n in s:
            if n != '.' and n not in square:
                square.add(n)
            elif n in square:
                return False
        return True