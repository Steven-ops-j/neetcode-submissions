from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        in_q = set()
        ans = 0
        for i in range(len(s)):
            if s[i] in in_q:
                while s[i] != q[0]:
                    in_q.remove(q.popleft())

                in_q.remove(q.popleft())
            q.append(s[i])
            in_q.add(s[i])
            ans = max(ans, len(q))
        return ans 
                
                    
                              