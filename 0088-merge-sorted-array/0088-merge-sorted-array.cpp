class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Copy nums2 elements into nums1
        for (int i = 0; i < n; i++) {
            nums1[m + i] = nums2[i];
        }

        // Sort nums1
        sort(nums1.begin(), nums1.end());
    }
};
