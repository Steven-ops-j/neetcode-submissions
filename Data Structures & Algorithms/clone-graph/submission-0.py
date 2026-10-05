"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        map_to_node = {}
        map_to_new_node = {}
        root = None
        def dfs(node):
            nonlocal root
            if not node or node.val in visited:
                return
            new_node = Node(node.val)
            if node.val == 1:
                root = new_node
            map_to_node[new_node] = node
            map_to_new_node[node.val] = new_node
            visited.add(node.val)
            for child in node.neighbors:
                dfs(child)
        dfs(node)
        for new_node, node in map_to_node.items():
            for child in node.neighbors:
                new_node.neighbors.append(map_to_new_node[child.val])
        return root