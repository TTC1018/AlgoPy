# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # List 변환 후 병합
        temp = []
        while list1:
            temp.append(list1.val)
            list1 = list1.next
        while list2:
            temp.append(list2.val)
            list2 = list2.next
        temp.sort()

        merged = None

        if len(temp) > 0:
            merged = ListNode(temp[0])
        if len(temp) > 1:
            merged.next = ListNode(temp[1])
            prev = merged.next
            for i in range(2, len(temp)):
                prev.next = ListNode(temp[i])
                prev = prev.next

        return merged

        # 재귀 풀이
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1