class Solution:

    def customSortString(self, order: str, s: str) -> str:

        l = list(order)
        k = list(s)
        m = ""

        for i in range(len(l)):
            if l[i] in k:
                m += l[i] * k.count(l[i])

        for j in range(len(k)):
            if k[j] not in m or k.count(k[j]) > m.count(k[j]):
                m += k[j]

        return m
