class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        m = min(height[left],height[right]) * (right -left)
        while left < right:
            if min(height[left],height[right]) * (right - left) > m:
                m = min(height[left],height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return m

        