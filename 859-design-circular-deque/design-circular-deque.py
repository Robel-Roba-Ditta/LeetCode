class MyCircularDeque:
    def __init__(self, k: int):
        self.capacity = k
        self.deque = [0] * k
        self.left = 0
        self.right = -1
        self.count = 0
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False      
        self.left = (self.left - 1 + self.capacity) % self.capacity
        self.deque[self.left] = value
        self.count += 1
        if self.count == 1:
            self.right = self.left
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.right = (self.right + 1) % self.capacity
        self.deque[self.right] = value
        self.count += 1
        if self.count == 1:
            self.left = self.right
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.left = (self.left + 1) % self.capacity
        self.count -= 1
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.right = (self.right - 1 + self.capacity) % self.capacity
        self.count -= 1
        return True
    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.left]
    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.right]
    def isEmpty(self) -> bool:
        return self.count == 0
    def isFull(self) -> bool:
        return self.count == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()