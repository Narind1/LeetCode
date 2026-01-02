class Solution {
public:
    int reverse(int x) {
        int remainder = 0;
        long reverse = 0;
        while(x!=0){
            remainder = x%10;
            reverse = reverse *10;
            reverse = reverse + remainder;
            x = x/10;
        }
        if (reverse<std::pow(-2,31) || reverse>std::pow(2,31)-1){
            return 0;
        }
    return reverse;
    }
};