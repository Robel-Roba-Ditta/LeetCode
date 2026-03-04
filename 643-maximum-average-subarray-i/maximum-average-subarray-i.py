class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        h = float('-inf')
        m = 0
        for i in range(k):
            m += nums[i]
        h = m
        left = 0
        for right in range(k, len(nums)):
            m += nums[right]
            m -= nums[left]

            h = max(h,m)
            left += 1
        avg = float(h/k)
        return avg
        
        