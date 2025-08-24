class Solution:
    def maxSubArray(self, nums):
        rn = nums[0]
        mx = nums[0]

        for i in range(1, len(nums)):
            if rn < 0:
                rn = 0
            rn += nums[i]
            mx = max(mx, rn)
        
        return mx