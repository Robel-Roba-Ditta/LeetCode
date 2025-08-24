import collections


class Solution:
    def permuteUnique(self, nums):
        result = []
        counter = collections.Counter(nums)

        def backtrack(perm, counter):
            if len(perm) == len(nums):
                result.append(perm[:])
                return

            for n in counter:
                if counter[n] == 0:
                    continue
                perm.append(n)
                counter[n] -= 1
                backtrack(perm, counter)
                perm.pop()
                counter[n] += 1

        backtrack([], counter)
        return result