class Solution:
    def minSteps(self, s: str, t: str) -> int:
        m = sorted(list(s))
        k = Counter(t)
        count = len(m)
        for i in m:
            if k[i] > 0:
                k[i] -= 1 
                count -= 1
        return count
        