class Solution:
    def searchInsert(self, nums, target):
        low, high = 0, len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low