from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        l = list(s)
        o = []
        c = Counter(l)

        for i, j in sorted(c.items(), key=lambda x: x[1], reverse=True):
            o.append(i * j)  

        return "".join(o)
