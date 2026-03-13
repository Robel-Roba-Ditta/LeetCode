class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        d = deque()
        f = deque()
        left = 0
        max_len = 0
        for right in range(len(nums)):
            while d and nums[right] < nums[d[-1]]:
                d.pop()
            while f and nums[right] > nums[f[-1]]:
                f.pop()
            d.append(right)
            f.append(right)
            while nums[f[0]] - nums[d[0]] > limit:
                left += 1
                if d[0] < left:
                    d.popleft()
                if f[0] < left:
                    f.popleft()
            max_len = max(max_len, right - left + 1)
        return max_len