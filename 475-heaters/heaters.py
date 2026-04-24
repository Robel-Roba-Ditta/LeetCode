class Solution:
    def findRadius(self, h, t):
        h.sort()
        t.sort()
        ans = 0
        for x in h:
            i = bisect.bisect_left(t, x)
            d1 = float('inf')
            d2 = float('inf')
            if i < len(t):
                d1 = abs(t[i] - x)
            if i > 0:
                d2 = abs(t[i-1] - x)
            ans = max(ans, min(d1, d2))
        return ans