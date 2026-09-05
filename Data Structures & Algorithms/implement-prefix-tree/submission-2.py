class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node(c, False)
            cur = cur.children.get(c)
        cur.isEnd = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children.get(c)
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        # print(cur, cur.children)
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children.get(c)
        return True
        

class Node:
    def __init__(self, val=None, isEnd=False, children=None):
        self.val = val
        self.isEnd = isEnd
        self.children = {} if children is None else children
        