class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def check_valid(s):
            cnt = 0
            for paren in s:
                if paren == ')':
                    cnt -= 1
                else:
                    cnt += 1
                if cnt < 0:
                    return False
            if cnt == 0:
                return True
        def permute(s):
            if len(s) == n * 2:
                if not check_valid(s):
                    return
                output.append("".join(s))
                return
            permute(s + ['('])
            permute(s + [')'])
        permute([])
        return output
                     