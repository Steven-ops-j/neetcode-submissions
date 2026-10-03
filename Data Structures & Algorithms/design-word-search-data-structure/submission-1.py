import string
class WordDictionary:

    def __init__(self):
        self.parent = Node('')

    def addWord(self, word: str) -> None:
        cur = self.parent
        for letter in word:
            if letter in cur.child:
                cur = cur.child[letter]
            else:
                node = Node(letter)
                cur.child[letter] = node
                cur = node
        cur.end = True 

    def search(self, word: str) -> bool:
        cur = self.parent
        def recurse(word, cur):
            for i in range(len(word)):
                letter = word[i]
                if letter in cur.child:
                    cur = cur.child[letter]
                elif letter == '.':
                    for possible in cur.child.keys():
                        if recurse(word[i+1:], cur.child[possible]):
                            return True
                    return False
                else:
                    return False
            if cur.end:
                return True
            return False
        return recurse(word, cur)

            
class Node:
    def __init__(self, letter):
        self.letter = letter
        self.child = {}
        self.end = False