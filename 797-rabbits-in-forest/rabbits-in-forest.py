class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        tot = 0
        for x, freq in c.items():
            s = x + 1
            g = math.ceil(freq / s)
            tot += g * s
        return tot