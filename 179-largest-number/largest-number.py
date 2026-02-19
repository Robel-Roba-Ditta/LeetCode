class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        l = []
        for i in nums:
            l.append(str(i))
        n = len(l)
        for i in range(n):
            for j in range(i + 1, n):
                if l[i] + l[j] < l[j] + l[i]:
                    l[i], l[j] = l[j], l[i]
        
        result = ''.join(l)
        if result[0] == '0':
            return '0'
        
        return result