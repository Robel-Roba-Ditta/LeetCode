class Solution:
    def pacificAtlantic(self, h):
        r = len(h)
        c = len(h[0])
        def bfs(starts):
            vis = set(starts)
            q = deque(starts)
            while q:
                x, y = q.popleft()
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < r and 0 <= ny < c:
                        if (nx, ny) not in vis and h[nx][ny] >= h[x][y]:
                            vis.add((nx, ny))
                            q.append((nx, ny))
            return vis
        pac = [(0, j) for j in range(c)] + [(i, 0) for i in range(r)]
        atl = [(r-1, j) for j in range(c)] + [(i, c-1) for i in range(r)]
        p = bfs(pac)
        a = bfs(atl)
        return list(p & a)