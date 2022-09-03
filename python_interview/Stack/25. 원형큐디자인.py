class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.front = 0
        self.rear = 0
        self.limit = k

    # queue 뒤 데이터 추가
    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:  # rear가 옮겨갈 자리 있을 때
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.limit
            return True
        else:
            return False

    # queue 앞 데이터 제거
    def deQueue(self) -> bool:
        if self.q[self.front] is None: # dequeue할 front data 없다면
            return False
        else:
            self.q[self.front] = None # dequeue 처리
            self.front = (self.front + 1) % self.limit # front 하나 밀어주기
            return True

    def Front(self) -> int:
        return self.q[self.front] if self.q[self.front] is not None else -1

    def Rear(self) -> int:
        return self.q[self.rear - 1] if self.q[self.rear - 1] is not None else -1

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()