from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        while queue:
            i, j, dis = queue.popleft()
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]) and grid[i][j] != -1 and (i, j) not in visited:
                grid[i][j] = dis
                for offset in [-1, 1]:
                    queue.append((i, j + offset, dis + 1))
                    queue.append((i + offset, j, dis + 1))
                
            visited.add((i, j))