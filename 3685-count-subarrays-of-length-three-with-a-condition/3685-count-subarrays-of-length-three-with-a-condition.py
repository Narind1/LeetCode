class Solution:
    def countSubarrays(self, nums):
        count = 0
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if b % 2 == 0 and a + c == b // 2:
                count += 1
        return count
