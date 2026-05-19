class MedianFinder:

    def __init__(self):
        self.l = []
        self.r = []

    def addNum(self, x):
        heapq.heappush(self.l, -x)
        
        heapq.heappush(self.r, -heapq.heappop(self.l))
        
        if len(self.r) > len(self.l):
            heapq.heappush(self.l, -heapq.heappop(self.r))

    def findMedian(self):
        if len(self.l) > len(self.r):
            return -self.l[0]
        
        return (-self.l[0] + self.r[0]) / 2