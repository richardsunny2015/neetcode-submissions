class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next  = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = self.right.prev = node
        node.prev = prev
        node.next = self.right

        self.cache[node.key] = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[node.key]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key].value
        self.remove(self.cache[key])
        self.insert(Node(key, val))
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.insert(Node(key, value))

        if len(self.cache) > self.capacity:
            k = self.left.next.key
            self.remove(self.cache[k])
