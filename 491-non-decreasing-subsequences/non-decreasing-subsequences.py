class Solution:
    def findSubsequences(self, nums):
        res = []
        def backtrack(start, path):
            if len(path) >= 2:
                res.append(path[:])
            sset = set()
            for i in range(start, len(nums)):
                if nums[i] in sset:
                    continue
                if not path or nums[i] >= path[-1]:
                    sset.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
        backtrack(0, [])
        return res