class Solution {
public:
    // void rotate(vector<int>& nums, int k) {
    //     for(int i=0;i<k;i++){
    //         int a = nums[nums.size()-1];
    //         for (int j=nums.size()-1;j>0;j--){
                
    //             nums[j]=nums[j-1];

    //         }
    //         nums[0]=a;
    //     }
    // }
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;

        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin() + k);
        reverse(nums.begin() + k, nums.end());
    }
};