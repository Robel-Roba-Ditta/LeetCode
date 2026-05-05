class Solution:
    def sortItems(self, n, m, group, before):
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        gi = defaultdict(list)
        for i in range(n):
            gi[group[i]].append(i)
        g_g = [[] for _ in range(m)]
        g_i = [[] for _ in range(n)]
        indeg_g = [0] * m
        indeg_i = [0] * n
        for i in range(n):
            for u in before[i]:
                g_i[u].append(i)
                indeg_i[i] += 1
                if group[u] != group[i]:
                    g_g[group[u]].append(group[i])
                    indeg_g[group[i]] += 1
        def topo(g, indeg):
            q = deque()
            res = []
            for i in range(len(indeg)):
                if indeg[i] == 0:
                    q.append(i)
            while q:
                u = q.popleft()
                res.append(u)
                for v in g[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
            return res if len(res) == len(indeg) else []
        og = topo(g_g, indeg_g)
        oi = topo(g_i, indeg_i)
        if not og or not oi:
            return []
        pos = {x: i for i, x in enumerate(oi)}
        for k in gi:
            gi[k].sort(key=lambda x: pos[x])
        res = []
        for g in og:
            res.extend(gi[g])
        return res