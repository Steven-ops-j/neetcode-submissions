class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = [[] for x in range(len(edges) + 1)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        def find_valid(removal): 
            stack = [1]
            visited = set()
            while stack:
                node = stack.pop()
                visited.add(node)
                cnt = 0
                flag = False
                for neighbor in adj_list[node]:
                    if [node, neighbor] == removal or [neighbor, node] == removal:
                        flag = True
                        continue
                    if neighbor in visited:
                        cnt += 1
                        continue
                    visited.add(neighbor)
                    stack.append(neighbor)
                if cnt == len(adj_list[node]) - flag and len(adj_list[node]) - flag > 1:
                    return False
            if len(visited) != len(edges):
                return False
            return True
        for i in range(len(edges) - 1, -1, -1):
            if find_valid(edges[i]):
                return edges[i]