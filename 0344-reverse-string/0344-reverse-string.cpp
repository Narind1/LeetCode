class Solution {
public:
    void reverseString(vector<char>& s) {
        int n = s.size()-1;
        int m =0;
        while(m<=n){
            int x = s[n];
            s[n] = s[m];
            s[m] = x;
            n--;
            m++;
        }
    }
};