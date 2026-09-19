class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + ','
            s += word
        return s
    def decode(self, s: str) -> List[str]:
        print(s)
        strs = []
        i = 0
        while i < len(s):
            l = 0
            while s[i] != ',':
                l *= 10
                l += int(s[i])
                i += 1
            word = ""
            i += 1
            while l > 0:
                word += s[i]
                i += 1
                l -= 1
            strs.append(word)
        return strs