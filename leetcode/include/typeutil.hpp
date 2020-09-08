#pragma once

#include <vector>

// Definition for singly-linked list.
namespace leetcode {
    struct ListNode {
        int val;
        ListNode *next;
        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode *next) : val(x), next(next) {}
    };

    ListNode *listGen(std::vector<int> source);

    bool listEqual(ListNode *n1, ListNode *n2);
}
