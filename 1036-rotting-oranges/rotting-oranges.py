class Solution:
    def orangesRotting(self, g):
        r = len(g)
        c = len(g[0])
        q = deque()
        f = 0
        for i in range(r):
            for j in range(c):
                if g[i][j] == 2:
                    q.append((i, j))
                elif g[i][j] == 1:
                    f += 1
        t = 0
        d = [(1,0), (-1,0), (0,1), (0,-1)]
        while q and f > 0:
            for _ in range(len(q)):
                x, y = q.popleft()     
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy      
                    if 0 <= nx < r and 0 <= ny < c and g[nx][ny] == 1:
                        g[nx][ny] = 2
                        f -= 1
                        q.append((nx, ny))
            t += 1
        return t if f == 0 else -1