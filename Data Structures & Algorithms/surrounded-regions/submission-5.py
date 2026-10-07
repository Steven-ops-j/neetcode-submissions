class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        visited = [[False] * len(x) for x in board]
        path = []
        def floodfill(i, j):
            cur = [[i, j]]
            flag = False
            while cur:  
                i, j = cur.pop()
                path.append([i, j])
                if i == n - 1 or j == m - 1 or i == 0 or j == 0:
                    flag = True
                visited[i][j] = True
                for x in [-1, 1]:
                    if i + x >= 0 and i + x < n and board[i + x][j] == 'O' and not visited[i + x][j]:
                        cur.append([i + x, j])
                    if j + x >= 0 and j + x < m and board[i][j + x] == 'O' and not visited[i][j + x]:
                        cur.append([i, j + x])
                 
            if flag:
                return
            for i, j in path:
                board[i][j] = 'X'
        for i in range(n):
            for j in range(m):
                path = []
                if not visited[i][j] and board[i][j] != 'X':
                    floodfill(i, j)
        