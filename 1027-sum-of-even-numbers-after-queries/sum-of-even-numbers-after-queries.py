# class Solution:
#     def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         r=[]
#         n= len(nums)
#         for val,ind in queries:
#             for i in range(n):
#                 t= 0
#                 if ind==i:
#                     nums[i]+=val[ind]
#                 if nums[i]%2==0:
#                     t+=nums[i]
#                     r.append(t)
#         print(r)
# class Solution:
#     def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         r = []
#         t = 0
#         for x in nums:
#             if x % 2 == 0:
#                 t += x

#         for val, ind in queries:
#             if nums[ind] % 2 == 0:
#                 t -= nums[ind]
#             nums[ind] += val
#             if nums[ind] % 2 == 0:
#                 t += nums[ind]
#             r.append(t)

#         return r
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        r = []
        t = 0
        for x in nums:
            if x % 2 == 0:
                t += x

        for val, ind in queries:
       
            if nums[ind] % 2 == 0:
                t -= nums[ind]
            nums[ind] += val
            if nums[ind] % 2 == 0:
                t += nums[ind]

            r.append(t)

        return r


            
           
        