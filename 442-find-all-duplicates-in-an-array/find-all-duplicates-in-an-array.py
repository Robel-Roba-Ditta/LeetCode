class Solution:
    def findDuplicates(self, nums):
        res = []
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0:
                res.append(abs(n))
            else:
                nums[idx] *= -1
        return res