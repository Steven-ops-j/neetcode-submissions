import string
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {}
        alphabet = string.ascii_lowercase
        for i in range(0, len(alphabet), 3):
            s = ""
            for j in range(i, min(len(alphabet), i + 3)):
                s += alphabet[j]
            dic[str(i // 3 + 2)] = s
        dic["7"] = "pqrs"
        dic["8"] = "tuv"
        dic["9"] = "wxyz"
        del dic["10"]
        output = []
        if not digits:
            return output
        def permute(s, cur):
            if not len(s):
                output.append("".join(cur))
                return
            letters = dic[s[0]]
            for j in range(len(letters)):
                permute(s[1:], cur + [letters[j]])
        permute(digits, [])
        return output