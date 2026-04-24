class Solution:
    def solveSudoku(self, b):
        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if b[i][j] != '.':
                    v = b[i][j]
                    r[i].add(v)
                    c[j].add(v)
                    box[(i//3)*3 + j//3].add(v)
        def dfs(i, j):
            if i == 9:
                return True
            ni = i + (j + 1) // 9
            nj = (j + 1) % 9
            if b[i][j] != '.':
                return dfs(ni, nj)
            for ch in '123456789':
                if ch not in r[i] and ch not in c[j] and ch not in box[(i//3)*3 + j//3]:
                    b[i][j] = ch
                    r[i].add(ch)
                    c[j].add(ch)
                    box[(i//3)*3 + j//3].add(ch)
                    if dfs(ni, nj):
                        return True
                    b[i][j] = '.'
                    r[i].remove(ch)
                    c[j].remove(ch)
                    box[(i//3)*3 + j//3].remove(ch)
            return False
        dfs(0, 0)