class Solution {
public:
 int minOperations(vector<int>& nums) {
    int n = nums.size();

        // Step 1: if overall GCD > 1 → impossible
        int overallGCD = nums[0];
        for (int i = 1; i < n; i++) {
            overallGCD = gcd(overallGCD, nums[i]);
        }
        if (overallGCD > 1) {
            return -1;
        }

        // Step 2: if there are already some 1's
        int count1 = count(nums.begin(), nums.end(), 1);
        if (count1 > 0) {
            return n - count1;
        }

        // Step 3: find smallest subarray with gcd == 1
        int minLen = n + 1;
        for (int i = 0; i < n; i++) {
            int g = nums[i];
            for (int j = i + 1; j < n; j++) {
                g = gcd(g, nums[j]);
                if (g == 1) {
                    minLen = min(minLen, j - i + 1);
                    break;
                }
            }
        }

        // Step 4: total operations
        return (minLen - 1) + (n - 1);
    }
};