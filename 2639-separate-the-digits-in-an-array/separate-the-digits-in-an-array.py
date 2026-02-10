class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            k = list(map(int, str(i)))
            l.extend(k)   
        return l
