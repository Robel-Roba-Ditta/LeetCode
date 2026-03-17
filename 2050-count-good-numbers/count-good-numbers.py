class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def power(x, n):
            if n == 0:
                return 1
            res = 1
            while n > 1:
                if n % 2:
                    res = (res * x) % MOD
                n = n // 2
                x = (x ** 2) % MOD
            return res * x
        even = (n + 1) // 2
        odd = n // 2
        return (power(5, even) * power(4, odd)) % MOD