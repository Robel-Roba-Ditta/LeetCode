class Solution:
    def kthSmallest(self, m, k):
        n = len(m)
        def cnt(x):
            i = n - 1
            j = 0
            c = 0
            while i >= 0 and j < n:
                if m[i][j] <= x:
                    c += i + 1
                    j += 1
                else:
                    i -= 1
            return c
        l = m[0][0]
        r = m[-1][-1]
        while l < r:
            mid = (l + r) // 2
            if cnt(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l