class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def f(l,r):
            if l==r:
                return nums[l]
            return max(nums[l]-f(l+1,r),nums[r]-f(l,r-1))
        return f(0,len(nums)-1)>=0
        