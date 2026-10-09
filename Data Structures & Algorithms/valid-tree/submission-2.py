class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for x in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        visited = set()
        s = []
        s.append(0)
        while s:
            node = s.pop()
            visited.add(node)
            cnt = 0
            for neighbor in adj_list[node]:
                if neighbor in visited:
                    cnt += 1
                    continue
                s.append(neighbor)
            if cnt == len(adj_list[node]) and len(adj_list[node]) > 1:
                return False
        if len(visited) < n:
            return False
        return True
                    
        
