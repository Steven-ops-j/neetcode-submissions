class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {'}': '{',
               ')': '(',
               ']': '['  }
        for bracket in s:
            if bracket in '[({':
                stack.append(bracket)
            else:
                
                if not stack or stack.pop() != mp[bracket]:
                    return False
        return not stack