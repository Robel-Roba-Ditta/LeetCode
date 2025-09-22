class NumArray:
    def __init__(self, nums):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)
        
    def sumRange(self, left, right):
        r = self.prefix[right] 
        l = self.prefix[left - 1] if left > 0 else 0
        return r - l