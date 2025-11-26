class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row(rowIndex + 1, 1);

        long long val = 1;
        for (int j = 1; j < rowIndex; j++) {
            val = val * (rowIndex - j + 1) / j;
            row[j] = val;
        }

        return row;
    }
};
