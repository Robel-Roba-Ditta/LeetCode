class Solution:
    def kSmallestPairs(self, a, b, k):
        if not a or not b:
            return []
        
        h = []
        
        for i in range(min(k, len(a))):
            heapq.heappush(h, (a[i] + b[0], i, 0))
        
        res = []
        
        while h and len(res) < k:
            _, i, j = heapq.heappop(h)
            
            res.append([a[i], b[j]])
            
            if j + 1 < len(b):
                heapq.heappush(h, (a[i] + b[j+1], i, j+1))
        
        return res