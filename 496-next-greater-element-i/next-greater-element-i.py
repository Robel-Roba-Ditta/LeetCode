class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        m = {}        
        for i in nums2:
            while stack and i > stack[-1]:
                m[stack.pop()] = i
            stack.append(i)
        while stack:
            m[stack.pop()] = -1
        
        res = []
        for i in nums1:
            res.append(m[i])
        
        return res

        