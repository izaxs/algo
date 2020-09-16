#include "common.hpp"

namespace leetcode {
    using std::cout;
    using std::endl;

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        auto fake = ListNode(), *cur = &fake;
        int carrier = 0;
        while (l1 || l2 || carrier) {
            if (l1) {
                carrier += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                carrier += l2->val;
                l2 = l2->next;
            }
            cur->next = new ListNode(carrier % 10);
            cur = cur->next;
            carrier = carrier / 10;
        }
        return fake.next;
    }
}

int main() {
    using namespace leetcode;
    auto head1 = listGen({1,5,4});
    cout << "list 1: " << to_string(head1) << endl;

    auto head2 = listGen({2,7});
    cout << "list 2: " << to_string(head2) << endl;

    auto expect = listGen({3,2,5});
    auto result = addTwoNumbers(head1, head2);

    cout << "predict: " << (listEqual(expect, result) ? "true" : "false") << endl;
    assert(to_string(expect) == to_string(result));
}