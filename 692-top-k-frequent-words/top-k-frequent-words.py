class Solution:
    def topKFrequent(self, w, k):
        mp = Counter(w)
        
        arr = sorted(mp.keys(), key=lambda x: (-mp[x], x))
        
        return arr[:k]