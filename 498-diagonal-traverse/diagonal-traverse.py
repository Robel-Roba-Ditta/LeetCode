class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]: 
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        row, col = 0, 0
        res = []
        u = True
        
        for _ in range(m * n):
            res.append(mat[row][col])
            if u:
                if col == n - 1:
                    row += 1
                    u = False
                elif row == 0: 
                    col += 1
                    u = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1:
                    col += 1
                    u = True
                elif col == 0: 
                    row += 1
                    u = True
                else:
                    row += 1
                    col -= 1
        return res
