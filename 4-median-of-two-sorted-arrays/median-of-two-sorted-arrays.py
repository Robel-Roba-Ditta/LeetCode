class Solution:
    def findMedianSortedArrays(self, a, b):
        if len(a) > len(b):
            a, b = b, a
        m = len(a)
        n = len(b)
        l = 0
        r = m
        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i
            l1 = float('-inf') if i == 0 else a[i-1]
            r1 = float('inf') if i == m else a[i]
            l2 = float('-inf') if j == 0 else b[j-1]
            r2 = float('inf') if j == n else b[j]
            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                r = i - 1
            else:
                l = i + 1