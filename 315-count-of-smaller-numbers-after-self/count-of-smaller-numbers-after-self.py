class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        res = [0] * n
        arr = list(enumerate(nums))  
        def merge_sort(l, r):
            if r - l <= 1:
                return arr[l:r]
            m = (l + r) // 2
            left = merge_sort(l, m)
            right = merge_sort(m, r)
            return merge(left, right)
        def merge(left, right):
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    res[left[i][0]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            while i < len(left):
                res[left[i][0]] += j
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1
            return merged
        merge_sort(0, n)
        return res