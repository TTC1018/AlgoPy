# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = odd_node = head
        if head:
            even_head = even_node = head.next
            while head and head.next and head.next.next:
                head = head.next.next
                even_node.next, odd_node.next = head.next, head
                even_node, odd_node = head.next, head
            odd_node.next = even_head
        return odd_head