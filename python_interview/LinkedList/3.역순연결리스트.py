# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None # 현재 노드, 이전 노드

        while node:
            next, node.next = node.next, prev # 현재 노드의 다음 노드 = 이전 노드
            node, prev = next, node # 현재 노드 = 다음 노드, 이전 노드 = 현재 노드
        return prev