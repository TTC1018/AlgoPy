# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 값만 교체
        node = head
        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
        return head

        # 노드 교체
        root = prev = ListNode()
        while head and head.next:
            # A - B 스왑한다고 가정
            nxt = head.next
            head.next = nxt.next # A가 B의 자리로 가므로, A의 다음은 B의 다음
            nxt.next = head # B의 다음은 A

            prev.next = new # A 이전의 다음은 B

            # 다음 스왑 노드로 이동
            head = head.next
            prev = prev.next.next
        return root.next

        # 재귀 풀이
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head