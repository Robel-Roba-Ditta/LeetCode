class RecentCounter:

    def __init__(self):
        self.s = deque()

    def ping(self, t: int) -> int:
        self.s.append(t)

        while self.s[0] < t - 3000:
            self.s.popleft()
    
        return len(self.s)