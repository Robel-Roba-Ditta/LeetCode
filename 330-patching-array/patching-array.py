class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        l = len(nums)
        m, p, i = 1, 0, 0
        while m <= n:
            if i < l and nums[i] <= m:
                m += nums[i]
                i += 1
            else:
                m += m
                p += 1
        return p