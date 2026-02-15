class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rc = len(mat)
        if len(mat) != len(target):
            return False
        
        for k in range(4):   

            if mat == target:   
                return True

            for i in range(rc):
                for j in range(i + 1, rc):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for rev in mat:
                rev.reverse()   

        return False

                    