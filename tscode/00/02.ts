import { ListNode } from "../lib"

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let dummy = new ListNode();
    let pre = dummy, c = 0;
    while (l1 || l2 || c) {
        if (l1) {
            c += l1.val;
            l1 = l1.next;
        }
        if (l2) {
            c += l2.val;
            l2 = l2.next;
        }
        pre.next = new ListNode(c % 10);
        c = c / 10 | 0;
        pre = pre.next;
    }
    return dummy.next;
};