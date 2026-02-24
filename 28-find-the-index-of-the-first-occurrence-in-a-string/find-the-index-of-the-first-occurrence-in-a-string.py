class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        left = 0
        while left <= n - m:
            right = 0
            while right < m and haystack[left + right] == needle[right]:
                right += 1
            if right == m:
                return left 
            left += 1

        return -1

        