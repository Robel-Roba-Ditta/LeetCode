class Solution:
    def isAdditiveNumber(self, s):
        n = len(s)
        for i in range(1, n):
            for j in range(i + 1, n):     
                a = s[:i]
                b = s[i:j] 
                if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
                    continue
                x = int(a)
                y = int(b)
                k = j
                while k < n:
                    z = x + y
                    t = str(z)
                    if not s.startswith(t, k):
                        break
                    k += len(t)
                    x, y = y, z
                if k == n:
                    return True
        return False