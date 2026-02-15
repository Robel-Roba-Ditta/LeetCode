class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r = len(img)
        c = len(img[0])
        new = [[0]*c for _ in range(r)]
        for h in range(r):
            for k in range(c):
                tot, cnt = 0, 0
                 
                for i in range(h-1, h+2):
                    for j in range(k-1, k+2):
                        if i< 0 or i==r or j<0 or j==c:
                            continue
                        tot += img[i][j]
                        cnt += 1
                new[h][k]= tot//cnt
        return new 
        