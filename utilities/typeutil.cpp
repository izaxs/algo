#include <vector>

namespace leetcode {
    // Definition for singly-linked list.
    struct ListNode {
        int val;
        ListNode *next;
        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode *next) : val(x), next(next) {}
    };

    ListNode *listGen(std::vector<int> source) {
        auto fake = new ListNode();
        auto cur = fake;
        for (int i : source) {
            cur->next = new ListNode(i);
            cur = cur->next;
        }
        return fake->next;
    }

    bool listEqual(ListNode *n1, ListNode *n2) {
        while (n1 != nullptr && n2 != nullptr) {
            if (n1->val != n2->val) return false;
            n1 = n1->next;
            n2 = n2->next;
        }
        if (n1 == nullptr && n2 == nullptr) return true;
        return false;
    }
}
