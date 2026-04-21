class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(index, prev):
            if index == len(s):
                return True
            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])
                if num == prev - 1:
                    if backtrack(i + 1, num):
                        return True
                elif num >= prev:
                    break
            return False
        for i in range(len(s) - 1):
            first = int(s[:i+1])
            if backtrack(i + 1, first):
                return True
        return False