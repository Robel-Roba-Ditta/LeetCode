class Solution:
    def lastStoneWeight(self, s):
        s = [-x for x in s]
        heapq.heapify(s)
        
        while len(s) > 1:
            a = -heapq.heappop(s)
            b = -heapq.heappop(s)
            
            if a != b:
                heapq.heappush(s, -(a - b))
        
        return -s[0] if s else 0