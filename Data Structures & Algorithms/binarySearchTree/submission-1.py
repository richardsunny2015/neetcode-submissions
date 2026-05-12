class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
            return
        def internal_insert(key, val, root):
            if not root:
                return TreeNode(key, val)
            if key < root.key:
                root.left = internal_insert(key, val, root.left)
            elif key > root.key:
                root.right = internal_insert(key, val, root.right)
            else:
                root.val = val
            return root
        self.root = internal_insert(key, val, self.root)

    def get(self, key: int) -> int:
        def traverse(root, key):
            if not root:
                return None
            if key < root.key:
                return traverse(root.left, key)
            elif key > root.key:
                return traverse(root.right, key)
            else:
                return root
        r = traverse(self.root, key)
        if r == None:
            return -1
        return r.val


    def getMin(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val


    def getMax(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val


    def remove(self, key: int) -> None:
        def minRoot(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        def deleteNode(root, key):
            if not root:
                return None
            if key > root.key:
                root.right = deleteNode(root.right, key)
            elif key < root.key:
                root.left = deleteNode(root.left, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    minNode = minRoot(root.right)
                    root.key = minNode.key
                    root.val = minNode.val
                    root.right = deleteNode(root.right, minNode.key)
            return root
        self.root = deleteNode(self.root, key)


    def getInorderKeys(self) -> List[int]:
        result = []
        def traverse(root):
            nonlocal result
            if not root:
                return
            traverse(root.left)
            result.append(root.key)
            traverse(root.right)
        traverse(self.root)
        return result

class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None