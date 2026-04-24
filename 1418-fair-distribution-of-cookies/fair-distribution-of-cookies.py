class Solution:
    def distributeCookies(self, c, k):
        n = len(c)
        arr = [0] * k
        res = float('inf')
        def dfs(i):
            nonlocal res
            if i == n:
                res = min(res, max(arr))
                return
            for j in range(k):
                arr[j] += c[i]
                if arr[j] < res:
                    dfs(i + 1)
                arr[j] -= c[i]
                if arr[j] == 0:
                    break
        dfs(0)
        return res