#include "common.hpp"

namespace leetcode {
    using namespace utilities;
    using std::string;
    using std::vector;

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        using alphabet = std::array<int, 26>;
        std::map<alphabet, vector<string>> table;
        vector<vector<string>> output;
        for (string &str : strs) {
            alphabet core{};
            for (char &ch : str) ++core[ch - 'a'];
            table[core].push_back(str);
        }
        output.reserve(table.size());
        for (auto &entry : table) output.push_back(entry.second);
        // Plain old loop is faster lol...
        // std::for_each(table.begin(), table.end(),
        //     [&](auto &entry) {output.push_back(entry.second);});
        return output;
    }

    // It's actually worse
    vector<vector<string>> groupAnagrams2(vector<string>& strs) {
        std::map<string, vector<string>> table;
        vector<vector<string>> output;
        for (string &str : strs) {
            int core[26]{};
            for (char &ch : str) ++core[ch - 'a'];
            string coreStr;
            for (int i = 0; i < 26; ++i) {
                if (core[i] > 0) coreStr += string(core[i], i + 'a');
            }
            table[coreStr].push_back(str);
        }
        output.reserve(table.size());
        for (auto &entry : table) output.push_back(entry.second);
        return output;
    }
}

int main() {
    using namespace leetcode;
    vector<string> input = {"bdddddddddd", "bbbbbbbbbbc"};
    auto output = groupAnagrams2(input);
    print_inputoutput(to_string(input), to_string(output));

    // vector<string> input = {"eat","tea","tan","ate","nat","bat"};
    // auto output = groupAnagrams2(input);
    // print_inputoutput(to_string(input), to_string(output));
}