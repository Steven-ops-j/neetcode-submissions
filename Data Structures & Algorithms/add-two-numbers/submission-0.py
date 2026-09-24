# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1 
        cur2 = l2
        prev = None
        carry = 0
        new_head = None
        while cur1 or cur2:
            val = 0
            if not cur1:
                val = cur2.val + carry
            elif not cur2:
                val = cur1.val + carry
            else:
                val = cur1.val + cur2.val + carry
            if val > 9:
                val %= 10
                carry = 1
            else:
                carry = 0

            new_node = ListNode(val)
            if prev:
                prev.next = new_node
            if not new_head:
                new_head = new_node
            prev = new_node
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        if carry:
            new_node = ListNode(carry)
            prev.next = new_node
        return new_head
            
            