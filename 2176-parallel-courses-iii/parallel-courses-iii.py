class Solution:
    def minimumTime(self, n, r, t):
        g = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in r:
            g[u-1].append(v-1)
            indeg[v-1] += 1
        q = deque()
        dp = [0] * n
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
                dp[i] = t[i]
        while q:
            u = q.popleft()
            for v in g[u]:
                dp[v] = max(dp[v], dp[u] + t[v])
                indeg[v] -= 1    
                if indeg[v] == 0:
                    q.append(v)
        return max(dp)