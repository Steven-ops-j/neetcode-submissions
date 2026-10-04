class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(x) for x in grid]
        ans = 0
        def floodfill(i, j, area):
            if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0:
                return area 
            if visited[i][j] or not grid[i][j]: 
                return area 
            visited[i][j] = True
            area += 1
            area = max(floodfill(i + 1, j, area), area)
            area = max(floodfill(i - 1, j, area), area)
            area = max(floodfill(i, j + 1, area), area)
            area = max(floodfill(i, j - 1, area), area)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j]:
                    ans = max(floodfill(i, j, 0), ans)
        return ans