class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - i - 1]:
                    return False
            return True
        output = []
        def permute(s, cur):
            if not len(s):
                if cur:
                    output.append(cur) 
            for i in range(len(s)):
                sub = s[:i + 1]
                if is_palindrome(sub):
                    permute(s[i + 1:], cur + [sub])
        permute(s, [])
        return output