class Solution:
    def shipWithinDays(self, w, d):
        def ok(c):
            days = 1
            cur = 0
            for x in w:
                if cur + x > c:
                    days += 1
                    cur = 0
                cur += x
            return days <= d
        l = max(w)
        r = sum(w)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            if ok(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans