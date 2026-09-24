# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        cur = None
        head = None
        if not list1:
            return list2
        if not list2:
            return list1
        if cur1.val <= cur2.val:
            cur = cur1
            head = cur1
            cur1 = cur1.next
        else:
            cur = cur2
            head = cur2
            cur2 = cur2.next

        while cur:
            if not cur1 and not cur2:
                break
            if cur1:
                cur1next = cur1.next
            if cur2:
                cur2next = cur2.next            
            if not cur1 or cur2 and cur2.val <= cur1.val:
                cur.next = cur2
                cur2 = cur2next
            else:
                cur.next = cur1
                cur1 = cur1next
            cur = cur.next
        return head
        
            
                