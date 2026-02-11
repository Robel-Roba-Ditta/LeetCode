class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        sset1 = set(nums1)
        sset2 = set(nums2)
        l1 = []
        l2 = []
        for i in sset1:
            if i not in sset2:
                l1.append(i)
        for j in sset2:
            if j not in sset1:
                l2.append(j)
        return [l1,l2]

        