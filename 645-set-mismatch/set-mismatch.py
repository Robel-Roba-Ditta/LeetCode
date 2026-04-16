class Solution:
    def findErrorNums(self, nums):
        s = set()
        dup = -1
        for n in nums:
            if n in s:
                dup = n
            s.add(n)
        for i in range(1, len(nums) + 1):
            if i not in s:
                return [dup, i]