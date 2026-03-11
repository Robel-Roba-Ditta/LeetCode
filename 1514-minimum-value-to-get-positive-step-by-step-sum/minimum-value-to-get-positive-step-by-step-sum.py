class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        p = 0
        s = 0
        for num in nums:
            p += num
            s = min(s, p)
        return 1 - s