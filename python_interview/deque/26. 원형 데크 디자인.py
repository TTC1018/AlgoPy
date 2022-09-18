class ListNode:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k = k
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.k == self.size:
            return False

        inserted = ListNode(value)
        nxt = self.head.next
        inserted.prev, inserted.next = self.head, nxt
        self.head.next, nxt.prev = inserted, inserted
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.k == self.size:
            return False

        inserted = ListNode(value)
        prv = self.tail.prev
        inserted.prev, inserted.next = prv, self.tail
        prv.next, self.tail.prev = inserted, inserted
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False

        nxt = self.head.next.next
        self.head.next = nxt
        nxt.prev = self.head
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False

        prv = self.tail.prev.prev
        self.tail.prev = prv
        prv.next = self.tail
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head.next.data if self.size else -1

    def getRear(self) -> int:
        return self.tail.prev.data if self.size else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k

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