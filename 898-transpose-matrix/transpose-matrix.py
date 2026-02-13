class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        cols = len(matrix[0])

        new = [[0]* row for _ in range(cols)]
        for i in range(row):
            for j in range(cols):
                new[j][i] = matrix[i][j]
        return new

        