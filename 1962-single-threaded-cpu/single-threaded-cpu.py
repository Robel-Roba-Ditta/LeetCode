class Solution:
    def getOrder(self, tasks):
        arr = []
        
        for i, (e, p) in enumerate(tasks):
            arr.append((e, p, i))
        
        arr.sort()
        
        h = []
        res = []
        t = 0
        i = 0
        n = len(arr)
        
        while i < n or h:
            
            if not h and t < arr[i][0]:
                t = arr[i][0]
            
            while i < n and arr[i][0] <= t:
                e, p, idx = arr[i]
                heapq.heappush(h, (p, idx))
                i += 1
            
            p, idx = heapq.heappop(h)
            t += p
            res.append(idx)
        
        return res