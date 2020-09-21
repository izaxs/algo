#include "common.hpp"

namespace leetcode {
    using namespace utilities;
    using std::unordered_set;
    using std::istringstream;
    using std::priority_queue;
    using std::unordered_map;

    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_set<string> ban(banned.begin(), banned.end());
        for (char &ch : paragraph) ch = isalpha(ch) ? tolower(ch) : ' ';
        istringstream input(paragraph);
        string token;
        unordered_map<string, int> table;
        while (input >> token) {
            if (ban.find(token) == ban.end()) table[token] += 1;
        }
        string output;
        int max = 0;
        for (auto pair : table) {
            if (pair.second > max) {
                max = pair.second;
                output = pair.first;
            }
        }
        return output;
    }
}

int main() {
    using namespace leetcode;
    string parag = "Bob hit a ball, the hit BALL flew far after it was hit.";
    vector<string> ban{"hit"};
    auto output =  mostCommonWord(parag, ban);
    string intputStr = "Paragraph:\n" + parag + "\nBan list:\n" + to_string(ban);
    print_inputoutput(intputStr, output);
}