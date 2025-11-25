class Solution {
public:
    int smallestRepunitDivByK(int k) {
        // Agar k 2 ya 5 se divisible hai to kabhi answer nahi milega
        if (k % 2 == 0 || k % 5 == 0) return -1;  
        
        int rem = 0;
        
        // Maximum k steps hi check karne honge
        for (int len = 1; len <= k; len++) {
            rem = (rem * 10 + 1) % k;  // naya 1 add kiya
            if (rem == 0) return len;  // divisible mil gaya
        }
        
        return -1; 
    }
};
