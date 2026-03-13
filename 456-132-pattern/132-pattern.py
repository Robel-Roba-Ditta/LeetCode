class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        l = nums[0]

        for j in range(1, len(nums)):

            while stack and nums[j] >= stack[-1][0]:
                stack.pop()

            if stack and nums[j] > stack[-1][1]:
                return True

            stack.append((nums[j], l))
            l = min(l, nums[j])

        return False