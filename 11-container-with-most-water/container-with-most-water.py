class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        most_water = 0
        while i <= j:
            most_water = max(most_water, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return most_water