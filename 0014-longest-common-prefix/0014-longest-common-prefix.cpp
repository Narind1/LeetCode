class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";  // edge case

        string prefix = strs[0]; // start with first string as prefix

        // loop through remaining strings
        for (int i = 1; i < strs.size(); i++) {
            int j = 0;

            // compare prefix and current string character by character
            while (j < prefix.size() && j < strs[i].size() && prefix[j] == strs[i][j]) {
                j++;
            }

            // shrink prefix to the common part
            prefix = prefix.substr(0, j);

            // if prefix becomes empty, no common prefix exists
            if (prefix.empty()) return "";
        }

        return prefix;
    }
};

