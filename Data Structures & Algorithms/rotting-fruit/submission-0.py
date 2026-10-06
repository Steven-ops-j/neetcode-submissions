from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        cnt = 0
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j, time))
                if grid[i][j] == 1:
                    cnt += 1
        while queue and cnt > 0:
            print(queue, cnt, visited)
            i, j, t = queue.popleft()
            if grid[i][j] == 1:
                cnt -= 1
            time = max(t, time)
            for x in [-1, 1]:
                if i + x >= 0 and i + x < len(grid):
                    if (i + x, j) not in visited and grid[i + x][j] == 1:
                        visited.add((i + x, j))
                        queue.append((i + x, j, time + 1))
                if j + x >= 0 and j + x < len(grid[0]):
                    if (i, j + x) not in visited and grid[i][j + x] == 1:
                        visited.add((i, j + x))
                        queue.append((i, j + x, time + 1))
        if cnt:
            return -1
        return time