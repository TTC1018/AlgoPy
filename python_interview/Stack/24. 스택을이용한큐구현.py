class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []  # input을 뒤집어서 넣는 장소

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()  # output이 비어있을 상태를 염두해서 peek 호출 (갱신)
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:  # output이 비어있으면 갱신해주기
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()