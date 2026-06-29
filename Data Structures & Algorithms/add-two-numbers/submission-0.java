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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        /*
            Do a while loop. If there is a next for 
            either lists, continue the loop.
            Go through each list and add the values at
            the pointer. If the sum is greater than 9,
            set carryover to true. Move pointer and if
            there is a carryover, add 1 to one of the numbers
            and set carryover to false.
            If one list is empty and the other isn't
        */
        ListNode head = new ListNode();
        ListNode current = head;
        int carryover = 0;

        while (l1 != null || l2 != null) {
            int sum = carryover;
            carryover = 0;
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
            if (sum > 9) {
                carryover = 1;
                sum %= 10;
            }
            current.val = sum;
            if (l1 == null && l2 == null) break;
            current.next = new ListNode();
            current = current.next;
        }
        if (carryover > 0) {
            current.next = new ListNode(carryover);
        }
        return head;
    }
}
