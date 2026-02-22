class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        l = sorted(piles, reverse= True)
        k = len(l)//3
        sum = 0
        for i in range(1, 1+ 2*k, 2):
            sum += l[i]
            
        return sum
