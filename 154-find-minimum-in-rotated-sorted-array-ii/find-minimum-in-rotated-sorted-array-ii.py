class Solution:
    def findMin(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[0]:
                return nums[i]
        return nums[0]