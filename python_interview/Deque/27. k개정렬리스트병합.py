from heapq import heappush, heappop


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answer = head = ListNode()

        q = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(q, (lists[i].val, i, lists[i]))

        while q:
            val, idx, h = heappop(q)
            head.next = h
            head = head.next

            if h.next:
                h = h.next
                heappush(q, (h.val, idx, h))

        return answer.next
