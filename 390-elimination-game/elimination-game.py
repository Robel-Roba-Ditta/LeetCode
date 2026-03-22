class Solution:
    def lastRemaining(self, n: int) -> int:
        def f(n,l):
            if n==1:
                return 1
            if l:
                return 2*f(n//2,0)
            return 2*f(n//2,1)-(0 if n%2 else 1)
        return f(n,1)
        