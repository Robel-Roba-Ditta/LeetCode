class Solution:
    def createSortedArray(self, ins):
        m = max(ins)
        bit = [0] * (m + 1)
        def upd(i):
            while i <= m:
                bit[i] += 1
                i += i & -i
        def qry(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s 
        res = 0
        mod = 10**9 + 7
        for i, x in enumerate(ins):
            l = qry(x - 1)
            r = i - qry(x)
            res = (res + min(l, r)) % mod
            upd(x)
        return res