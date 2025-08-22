class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                return [i, hashmap[target - nums[i]]]
            hashmap[nums[i]] = i
