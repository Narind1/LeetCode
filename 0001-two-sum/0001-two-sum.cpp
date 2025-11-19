class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // for (int i = 0; i < nums.size(); i++) {
        //     for (int j = i + 1; j < nums.size(); j++) {
        //         if (nums[i] + nums[j] == target) {
        //             return {i, j};
        //         }
        //     }
        // }
        // return {};
        unordered_map<int, int> mp;  // value -> index

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            // Check if the complement already exists
            if (mp.count(complement)) {
                return {mp[complement], i};
            }

            // Store current number with its index
            mp[nums[i]] = i;
        }

        return {};
    }
};
