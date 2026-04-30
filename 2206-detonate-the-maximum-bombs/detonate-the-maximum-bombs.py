class Solution:
    def maximumDetonation(self, b):
        n = len(b)
        g = [[] for _ in range(n)]
        for i in range(n):
            x1, y1, r1 = b[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = b[j]
                if (x1 - x2)**2 + (y1 - y2)**2 <= r1**2:
                    g[i].append(j)
        def dfs(i, vis):
            vis.add(i)
            for nei in g[i]:
                if nei not in vis:
                    dfs(nei, vis)
        ans = 0
        for i in range(n):
            vis = set()
            dfs(i, vis)
            ans = max(ans, len(vis))
        return ans