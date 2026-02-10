class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = list(s)
        k = list(t)
        if sorted(l)==sorted(k):
            return True
        else:
            return False 
        