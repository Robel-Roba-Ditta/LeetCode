class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        p_sum=defaultdict(int)
        p_sum[0]=-1
        summ=0

        for  r in range(len(nums)):
            summ+=nums[r]
            
            if summ%k in p_sum:
                if r-p_sum[summ%k]>=2:
                    return True
            else:
                p_sum[summ%k]=r
        
        return False