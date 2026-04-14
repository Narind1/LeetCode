// class Solution {
// public:
    // int longestCommonSubsequence(string text1, string text2) {
    //     return helper(text1, text2,text1.size(),text2.size());
    // }
    // int helper(string text1,string text2,int m, int n){
    //     if(m == 0 || n == 0){
    //         return 0;
    //     }
    //     if(text1[m-1]==text2[n-1])
    //         return 1 + helper(text1,text2,m-1,n-1);
        
    //         return max(helper(text1,text2,m-1,n),helper(text1,text2,m,n-1));
    // }
class Solution {
public:
    vector<vector<int>> dp;

    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.size();
        int n = text2.size();

        dp.resize(m+1, vector<int>(n+1, -1));

        return helper(text1, text2, m, n);
    }

    int helper(string &text1, string &text2, int m, int n) {
        if (m == 0 || n == 0) {
            return 0;
        }

        if (dp[m][n] != -1) {
            return dp[m][n];
        }

        if (text1[m-1] == text2[n-1]) {
            return dp[m][n] = 1 + helper(text1, text2, m-1, n-1);
        }

        return dp[m][n] = max(
            helper(text1, text2, m-1, n),
            helper(text1, text2, m, n-1)
        );
    }
};
// };