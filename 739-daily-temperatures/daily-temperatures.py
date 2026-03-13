class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        s = {}
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                s[prev_day] = i - prev_day
            stack.append(i)
        for i in stack:
           s[i] = 0
        return [s[i] for i in range(n)]