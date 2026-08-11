class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        return self.recurse(self.root, word)
    
    def recurse(self, root, word):
        if not root:
            return False
        if not word:
            return root.word
        c = word[0]
        result = False
        if c == ".":
            for k in root.children.keys():
                result = result or self.recurse(root.children[k], word[1:])
        elif c in root.children:
            result = self.recurse(root.children[c], word[1:])
        
        return result
        