class Solution:
    def getSkyline(self, b):
        e = []
        
        for l, r, h in b:
            e.append((l, -h, r))
            e.append((r, 0, 0))
        
        e.sort()
        
        h = [(0, float('inf'))]
        res = []
        
        for x, nh, r in e:
            
            while h[0][1] <= x:
                heapq.heappop(h)
            
            if nh:
                heapq.heappush(h, (nh, r))
            
            cur = -h[0][0]
            
            if not res or res[-1][1] != cur:
                res.append([x, cur])
        
        return res