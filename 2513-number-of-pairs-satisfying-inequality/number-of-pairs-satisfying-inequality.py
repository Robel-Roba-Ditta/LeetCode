class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        arr = [a - b for a, b in zip(nums1, nums2)]
        self.count = 0
        def merge_sort(l, r):
            if r - l <= 1:
                return arr[l:r]
            m = (l + r) // 2
            left = merge_sort(l, m)
            right = merge_sort(m, r)
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > right[j] + diff:
                    j += 1
                self.count += len(right) - j
            return sorted(left + right)
        merge_sort(0, len(arr))
        return self.count