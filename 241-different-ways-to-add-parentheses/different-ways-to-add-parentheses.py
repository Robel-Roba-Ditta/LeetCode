class Solution:
    def diffWaysToCompute(self, s):
        def f(s):
            res = []
            for i, c in enumerate(s):
                if c in '+-*':
                    for l in f(s[:i]):
                        for r in f(s[i + 1:]):
                            res.append(eval(str(l) + c + str(r)))
            
            return res or [int(s)]
        return f(s)