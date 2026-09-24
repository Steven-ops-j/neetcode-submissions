class LRUCache:

    def __init__(self, capacity: int):
        self.head = None 
        self.tail = None
        self.sz = 0
        self.mp = {}
        self.cap = capacity

    def move_to_tail(self, node):
        if self.head == node:
            self.head = self.head.next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        node = self.mp[key] 
        if self.sz > 1 and self.tail is not node:
            self.move_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.mp[key].val = value
            if self.sz > 1 and self.tail is not self.mp[key]:
                self.move_to_tail(self.mp[key])
            return
        self.sz += 1
        node = Node(key, value)
        self.mp[key] = node
        if self.head == None:
            self.head = node
            self.tail = node
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        if self.sz > self.cap:
            headnext = self.head.next
            del self.mp[self.head.key]
            self.head.next = None
            self.head = headnext
            self.head.prev = None
            self.sz -= 1

class Node:
    def __init__(self, key: int, val: int, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev