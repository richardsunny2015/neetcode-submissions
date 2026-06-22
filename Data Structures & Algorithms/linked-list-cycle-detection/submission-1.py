# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if not head:
        #     return False
        # if "visited" in head and head.visited:
        #     return True
        # head.visited = True
        # return self.hasCycle(head.next)
        visited = set()

        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
            
        return False
        