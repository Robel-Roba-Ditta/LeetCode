class Solution:
    def rotate(self, matrix):
        i = 0
        while i < len(matrix)//2:
            j = len(matrix) - 1 - i
            l = 0
            while l < j-i:
                matrix[i+l][j], matrix[j][j-l], matrix[j-l][i], matrix[i][i+l] = matrix[i][i+l], matrix[i+l][j], matrix[j][j-l], matrix[j-l][i]
                l += 1
            i += 1