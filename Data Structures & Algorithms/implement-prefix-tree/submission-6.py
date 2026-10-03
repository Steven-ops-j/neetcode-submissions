class PrefixTree:

    def __init__(self):
        self.parent = Node('')
    def insert(self, word: str) -> None:
        cur = self.parent
        for letter in word:
            ind = -1
            for i in range(len(cur.child)):
                if cur.child[i] and cur.child[i].letter == letter:
                    ind = i
                    break
            if ind == -1:
                node = Node(letter)
                cur.child.append(node)
                cur = node
            else:
                cur = cur.child[ind]
        cur.child.append(None)
    def search(self, word: str) -> bool:
        cur = self.parent
        for letter in word:
            ind = -1
            for i in range(len(cur.child)):
                if cur.child[i] and cur.child[i].letter == letter:
                    ind = i
                    break
            if ind == -1:
                return False
            else:
                cur = cur.child[ind]
        if not cur.child or None in cur.child:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.parent
        for letter in prefix:
            ind = -1
            for i in range(len(cur.child)):
                if cur.child[i] and cur.child[i].letter == letter:
                    ind = i
                    break
            if ind == -1:
                return False
            else:
                cur = cur.child[ind]
        return True
        
class Node:
    def __init__(self, letter, child=None):
        self.letter = letter
        self.child = child if child else []
    