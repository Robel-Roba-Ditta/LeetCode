class Solution:
    def removeInvalidParentheses(self, s: str):
        res = set()
        def count_invalid(s):
            l = r = 0
            for c in s:
                if c == '(':
                    l += 1
                elif c == ')':
                    if l == 0:
                        r += 1
                    else:
                        l -= 1
            return l, r
        l, r = count_invalid(s)
        def backtrack(i, path, l_rem, r_rem, balance):
            if i == len(s):
                if l_rem == 0 and r_rem == 0 and balance == 0:
                    res.add(path)
                return
            c = s[i]
            if c == '(' and l_rem > 0:
                backtrack(i+1, path, l_rem-1, r_rem, balance)
            elif c == ')' and r_rem > 0:
                backtrack(i+1, path, l_rem, r_rem-1, balance)
            if c == '(':
                backtrack(i+1, path+c, l_rem, r_rem, balance+1)
            elif c == ')':
                if balance > 0:
                    backtrack(i+1, path+c, l_rem, r_rem, balance-1)
            else:
                backtrack(i+1, path+c, l_rem, r_rem, balance)
        backtrack(0, "", l, r, 0)
        return list(res)