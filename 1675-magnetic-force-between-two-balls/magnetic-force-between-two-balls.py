class Solution:
    def maxDistance(self, p, m):
        p.sort()
        def ok(d):
            c = 1
            last = p[0]
            for i in p:
                if i - last >= d:
                    c += 1
                    last = i
            return c >= m
        l = 1
        r = p[-1] - p[0]
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if ok(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans