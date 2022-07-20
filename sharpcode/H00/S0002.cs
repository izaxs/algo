namespace SharpCode;
public class S0002
{
    public ListNode? AddTwoNumbers(ListNode? l1, ListNode? l2)
    {
        var head = new ListNode();
        var cur = head;
        var carry = 0;
        while (l1 is not null || l2 is not null || carry != 0)
        {
            carry += l1?.val ?? 0;
            l1 = l1?.next;
            carry += l2?.val ?? 0;
            l2 = l2?.next;
            cur.next = new ListNode(carry % 10);
            carry /= 10;
            cur = cur.next;
        }
        return head.next;
    }

    public ListNode? AddTwoNumbersSmall(ListNode? l1, ListNode? l2)
    {
        var head = new ListNode();
        var cur = head;
        var carry = 0;
        while (l1 is not null || l2 is not null || carry != 0)
        {
            carry += l1?.val ?? 0;
            carry += l2?.val ?? 0;
            cur.next = l1 ?? l2 ?? new ListNode();
            cur.next.val = carry % 10;
            carry /= 10;
            l1 = l1?.next;
            l2 = l2?.next;
            cur = cur.next;
        }
        return head.next;
    }

    public ListNode? AddTwoNumbersFast(ListNode? l1, ListNode? l2)
    {
        var head = new ListNode();
        var cur = head;
        var carry = 0;
        while (l1 is not null || l2 is not null)
        {
            if (l1 is not null)
            {
                carry += l1.val;
                cur.next = l1;
                l1 = l1.next;
            }
            if (l2 is not null)
            {
                carry += l2.val;
                cur.next = l2;
                l2 = l2.next;
            }
            cur.next!.val = carry % 10;
            carry /= 10;
            cur = cur.next;
        }
        if (carry != 0)
        {
            cur.next = new ListNode(carry);
        }
        return head.next;
    }
}
