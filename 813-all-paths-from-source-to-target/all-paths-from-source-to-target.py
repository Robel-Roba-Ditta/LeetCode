class Solution:
    def allPathsSourceTarget(self, g):
        n = len(g)
        res = []
        def dfs(i, path):
            if i == n - 1:
                res.append(path[:])
                return
            for nei in g[i]:
                path.append(nei)
                dfs(nei, path)
                path.pop()
        dfs(0, [0])
        return res