# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        cur = head
        while cur:
            cur = cur.next
            sz += 1
        cur = head
        cnt = 1
        while cnt < sz - n:
            cur = cur.next
            cnt += 1
        if sz - n == 0:
            head = head.next
            return head
        cur.next = cur.next.next
        return head
