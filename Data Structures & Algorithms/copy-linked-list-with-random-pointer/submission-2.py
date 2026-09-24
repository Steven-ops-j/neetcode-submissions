"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {} 
        new_head = None
        prev = None
        while head:
            new_node = None
            if head in seen:
                new_node = seen[head]
            else:
                new_node = Node(head.val, None, None)
            seen[head] = new_node

            if prev:
                prev.next = new_node
            if head.random != None:
                if head.random in seen:
                    new_node.random = seen[head.random]
                else:
                    random_node = Node(head.random.val, None, None)
                    seen[head.random] = random_node
                    new_node.random = random_node
            if not prev:
                new_head = new_node
            prev = new_node
            head = head.next
        return new_head 