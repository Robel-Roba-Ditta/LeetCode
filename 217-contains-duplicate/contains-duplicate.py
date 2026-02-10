class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for i in nums:
            if c[i] >= 2:
                return True
                break
        return False
        