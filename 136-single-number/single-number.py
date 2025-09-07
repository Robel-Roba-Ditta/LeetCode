class Solution:
    def singleNumber(self, nums):
        res = 0
        for n in nums:
            res = n ^ res
        return res