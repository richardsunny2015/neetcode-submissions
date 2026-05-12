class Deque:
    
    def __init__(self):
        self.tail = None
        self.head = None


    def isEmpty(self) -> bool:
        return self.head == None

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        

    def pop(self) -> int:
        if self.tail == None:
            return -1
        original_tail = self.tail
        self.tail = self.tail.prev
        if self.tail == None:
            self.head = None
        else:
            self.tail.next = None
        return original_tail.val

    def popleft(self) -> int:
        if self.head == None:
            return -1
        original_head = self.head
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        else:
            self.head.prev = None
        return original_head.val
        
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None