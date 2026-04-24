class Solution:
    def smallestNumber(self, p):
        st = []
        res = []
        for i in range(len(p) + 1):
            st.append(str(i + 1))
            if i == len(p) or p[i] == 'I':
                while st:
                    res.append(st.pop())
        return ''.join(res)