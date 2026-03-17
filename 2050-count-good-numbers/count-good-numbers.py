class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even = (n + 1) // 2
        odd = n // 2
        def power(base, exp):
            result = 1
            while exp:
                if exp % 2:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return result
        
        return (power(5, even) * power(4, odd)) % MOD