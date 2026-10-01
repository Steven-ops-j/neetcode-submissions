class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)
        def permute(i, j, s, visited):
            if s == word:
                return True
            if i >= len(board) or i < 0 or j >= len(board[i]) or j < 0:
                return False
            if (i, j) in visited:
                return False
            if s != word[:len(s)]:
                return False
            visited | {board[i][j]} 
            return permute(i + 1, j, s + [board[i][j]], visited | {(i, j)}) or permute(i - 1, j, s + [board[i][j]], visited | {(i, j)}) or permute(i, j - 1, s + [board[i][j]], visited | {(i, j)}) or permute(i, j + 1, s + [board[i][j]], visited | {(i, j)})
        for i in range(len(board)):
            for j in range(len(board[i])):
                if permute(i, j, [], set()):
                    return True
        return False