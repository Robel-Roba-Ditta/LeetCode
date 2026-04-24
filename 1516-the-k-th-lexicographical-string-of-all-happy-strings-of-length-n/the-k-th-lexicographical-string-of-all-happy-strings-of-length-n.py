class Solution:
    def getHappyString(self, n, k):
        res = []
        def dfs(s):
            if len(s) == n:
                res.append(s)
                return
            for ch in 'abc':
                if not s or s[-1] != ch:
                    dfs(s + ch)
        dfs('')
        return res[k-1] if k <= len(res) else ''