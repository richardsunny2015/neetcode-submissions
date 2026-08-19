class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.recency = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache[key][1] = self.recency
        self.recency += 1
        return self.cache[key][0]
 
    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            print(len(self.cache), key)
            least_recent = sys.maxsize
            least = None
            for k, v in self.cache.items():
                _, recency = v
                if recency < least_recent:
                    least_recent = recency
                    least = k
            self.cache.pop(least)
        self.cache[key] = [value, self.recency]
        self.recency += 1


