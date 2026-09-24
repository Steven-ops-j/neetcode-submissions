# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        pos = 1
        cur = head
        while pos <= (n - 1) // 2 + 1:
            last = cur
            cnt = 0
            while cnt < n - 2 * pos + 1:
                last = last.next
                cnt += 1
            curnext = cur.next
            cur.next = last
            if curnext == last or cur == last:
                last.next = None
            else:
                last.next = curnext
            cur = curnext
            pos += 1