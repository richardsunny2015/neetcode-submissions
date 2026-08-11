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
        return self.recurse(self.root, word, 0)
    
    def recurse(self, root, word, ind):
        if not root:
            return False
        if ind == len(word):
            return root.word
        c = word[ind]
        result = False
        if c == ".":
            for k in root.children.keys():
                result = result or self.recurse(root.children[k], word, ind + 1)
        elif c in root.children:
            result = self.recurse(root.children[c], word, ind + 1)
        
        return result
        