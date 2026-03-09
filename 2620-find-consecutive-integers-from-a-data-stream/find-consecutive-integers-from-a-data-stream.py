class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.s = 0
        

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.s += 1
        else:
            self.s = 0
        return self.s >= self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)