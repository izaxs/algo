#include "common.hpp"

namespace leetcode {
    using namespace utilities;
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
    auto input1 = listGen({1,5,4});
    auto input2 = listGen({2,7});
    auto expect = listGen({3,2,5});
    auto output = addTwoNumbers(input1, input2);
    cout << "result: " << (listEqual(expect, output) ? "true" : "false") << endl;
}