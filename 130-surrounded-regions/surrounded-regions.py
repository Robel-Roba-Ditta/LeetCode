class Solution:
    def solve(self, board):
        rows, cols = len(board), len(board[0])
        flag = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                board[r][c] != 'O' or (r, c) in flag):
                return
            flag.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if ((r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and 
                    board[r][c] == 'O'):
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in flag:
                    board[r][c] = 'X'