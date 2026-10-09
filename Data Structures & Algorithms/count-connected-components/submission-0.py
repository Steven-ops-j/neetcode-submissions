class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for x in range(n)]

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()
        cnt = 0
        for i in range(n):
            if i in visited:
                continue
            cnt += 1
            stack = [i]
            while stack:
                node = stack.pop()
                for neighbors in adj_list[node]:
                    if neighbors in visited:
                        continue
                    visited.add(neighbors)
                    stack.append(neighbors)
        return cnt
            