from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Deque 풀이
        # q = deque()
        # q.append(head.val)
        #
        # nxt = head.next
        # while nxt != None:
        #     q.append(nxt.val)
        #     nxt = nxt.next
        #
        # while len(q) > 1:
        #     if q.popleft() != q.pop():
        #         return False
        # return True

        # 연결 리스트 그대로 사용
        slow = fast = head
        rev = None

        while fast and fast.next:
            fast = fast.next.next
            rev, slow.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
