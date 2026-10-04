class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(x) for x in grid]
        ans = 0
        def floodfill(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0:
                return
            if visited[i][j] or grid[i][j] == "0":
                return 
            visited[i][j] = True
            floodfill(i + 1, j)
            floodfill(i - 1, j)
            floodfill(i, j + 1)
            floodfill(i, j - 1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j] == "1":
                    floodfill(i, j)
                    ans += 1
        return ans