class Solution:
    def wordBreak(self, s, w):
        st = set(w)
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                return ['']
            res = []
            for j in range(i + 1, len(s) + 1):
                t = s[i:j]
                if t in st:
                    for sub in dfs(j):
                        if sub:
                            res.append(t + ' ' + sub)
                        else:
                            res.append(t)
            dp[i] = res
            return res
        return dfs(0)