class Solution:
    def furthestBuilding(self, h, b, l):
        heap = []
        for i in range(len(h) - 1):
            d = h[i + 1] - h[i]
            if d <= 0:
                continue
            heapq.heappush(heap, d)
            if len(heap) > l:
                b -= heapq.heappop(heap)
            if b < 0:
                return i
        return len(h) - 1