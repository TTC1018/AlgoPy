# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head:
            root = start = ListNode()
            root.next = head
            for _ in range(left - 1):
                start = start.next
            end = start.next

            for _ in range(right - left):
                tmp, start.next, end.next = start.next, end.next, end.next.next
                # start의 다음 노드를 임시 저장,
                # 그 후 start의 다음 노드를 end의 다음 노드로 설정
                # 그리고 end였던 노드를 한칸 밀어냄 (start.next의 다음 노드로 설정)

                start.next.next = tmp # start의 바로 뒤에 있던 노드가 새로운 노드에게 밀려남 (새 노드의 다음 노드가 됨)

        return root.next