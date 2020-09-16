#pragma once
#include <string>
#include <vector>

namespace utilities {
    using std::string;
    using std::vector;

    // declarations of stringifiers for item types
    string to_string(const string &s);

    string to_string(const char* t);

    string to_string(ListNode *head);

    string to_string(bool b);

    // template stringifiers for item types
    template<typename T>
    string to_string(const T &item) {
        return std::to_string(item);
    }

    // template stringifiers for container types
    template<typename T>
    string to_string(vector<T> items) {
        string output = "{ ";
        for (int i = 0; i < items.size(); i++) {
            output += to_string(items[i]);
            if (i != items.size() - 1) {
                output += ", ";
            }
        }
        output += " }";
        return output;
    }
}