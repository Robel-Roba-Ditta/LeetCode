class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        nums = sorted(nums)
        length = len(nums) - 1
        index = 0
        for i, n in enumerate(nums):
            if n >= 0:
                index = i
                break
        d = nums[index]
        if d > 1:
            return 1
        for i, n in enumerate(nums[index + 1:]):
            if d + 1 == n or d == n:
                d = n
            else:
                break
        return d + 1 if d + 1 > 0 else 1