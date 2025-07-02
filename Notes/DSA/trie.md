# Trie (pronouned try)

A Tree like data structure in which every node is suffix value and every branch has its own value attched to it. The Suffix value is nothing but collective value of all the branches travelled to get to that node. 

()---a--->(a)----b--->(ab)----

Unlike above example there can be multiple branches after each node

Unlike binary Tree or BST, a trie root node can have multiple child nodes. 

Boolean value describing whether its a complete words.


```python
class TrieNode:
    def __init__(self, prefix, child_characters:list=None, is_complete:bool=False):
        self.nodes = dict()
        self.is_complete = 

```


```python
class TreiNode:
    def __init__(self):
        # self.val = None
        self.children = {}
        self.is_complete = False # this is true only if its leaf node


class PrefixTree:

    def __init__(self):
        # self.val = None
        # self.children = 
        self.root = TreiNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreiNode()
            cur = cur.children[c]
        cur.is_complete = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.is_complete

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True
```
