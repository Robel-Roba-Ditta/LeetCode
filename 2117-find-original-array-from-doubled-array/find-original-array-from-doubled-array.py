class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        freq = Counter(changed)
        res = []

        for x in sorted(changed):
            if freq[x] == 0:
                continue

            if freq[2 * x] == 0:
                return []

            res.append(x)
            freq[x] -= 1
            freq[2 * x] -= 1

        return res