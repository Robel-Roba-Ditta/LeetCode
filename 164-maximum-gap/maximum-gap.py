class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()
        difference = 0
        for i in range(1, len(nums)):
            difference = max(difference, nums[i] - nums[i-1])
        return difference