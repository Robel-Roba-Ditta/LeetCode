class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        l = sorted(set(nums))   
        
        max_count = 1
        count = 1

        for i in range(len(l) - 1):
            if l[i] == l[i + 1] - 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1   

        max_count = max(max_count, count)
        return max_count