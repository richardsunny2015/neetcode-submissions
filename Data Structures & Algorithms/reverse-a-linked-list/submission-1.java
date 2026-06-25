/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) return null;
        return reverse(head, null);
    }
    private ListNode reverse(ListNode head, ListNode prev) {
        ListNode newHead = head;
        if (newHead.next != null) {
            newHead = reverse(head.next, head);
        }
        head.next = prev;
        return newHead;
    }
}
