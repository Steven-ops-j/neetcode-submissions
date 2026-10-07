class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pvisited = [[False] * len(x) for x in heights]
        avisited = [[False] * len(x) for x in heights]
        n = len(heights)
        m = len(heights[0])
        def floodfill(i, j, visited, prev):
            if i >= n or i < 0 or j >= m or j < 0:
                return
            if visited[i][j]:
                return
            if heights[i][j] < prev:
                return 
            visited[i][j] = True
            floodfill(i + 1, j, visited, heights[i][j])
            floodfill(i - 1, j, visited, heights[i][j])
            floodfill(i, j + 1, visited, heights[i][j])
            floodfill(i, j - 1, visited, heights[i][j])
        for i in range(m):
            if not pvisited[0][i]:
                floodfill(0, i, pvisited, 0)
        for i in range(n):
            if not pvisited[i][0]:
                floodfill(i, 0, pvisited, 0)
        for i in range(m):
            if not avisited[n - 1][i]:
                floodfill(n - 1, i, avisited, 0)
        for i in range(n):
            if not avisited[i][m - 1]:
                floodfill(i, m - 1, avisited, 0)
        output = []
        for i in range(n):
            for j in range(m):
                if pvisited[i][j] and avisited[i][j]:
                    output.append([i, j])
        return output