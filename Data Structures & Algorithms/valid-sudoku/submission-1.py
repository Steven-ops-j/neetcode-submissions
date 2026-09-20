class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s and board[i][j] != '.':
                    return False
                s.add(board[i][j])
        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] in s and board[i][j] != '.':
                    return False
                s.add(board[i][j])
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] in s and board[k][l] != '.':
                            return False
                        s.add(board[k][l])

        return True
                        