class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        /*for(int i=0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                if(nums[i]==nums[j]){
                    if(abs(i-j)<=k){
                        return true;
                    }
                }
            }
        }*/
        unordered_set<int> window;
        for (int i = 0; i < nums.size(); i++) {
            if (window.count(nums[i])) return true;
            window.insert(nums[i]);
            if (window.size() > k) {
                window.erase(nums[i - k]);
            }
        }
        return false;
     }

};