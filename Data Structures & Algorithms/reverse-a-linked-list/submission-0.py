# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        return self.reverse(head, None)
    def reverse(self, node, prev):
        new_head = node
        if node.next:
            new_head = self.reverse(node.next, node)
        node.next = prev
        return new_head