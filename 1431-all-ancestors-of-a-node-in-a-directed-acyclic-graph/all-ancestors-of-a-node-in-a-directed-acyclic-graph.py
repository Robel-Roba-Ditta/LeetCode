class Solution:
    def getAncestors(self, n, edges):
        g = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            g[u].append(v)
            indeg[v] += 1
        anc = [set() for _ in range(n)]
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        while q:
            u = q.popleft()
            for v in g[u]:
                anc[v].update(anc[u])
                anc[v].add(u)
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return [sorted(list(x)) for x in anc]