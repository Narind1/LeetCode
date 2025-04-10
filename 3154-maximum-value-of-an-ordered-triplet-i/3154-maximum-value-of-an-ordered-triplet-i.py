class Solution(object):
    def maximumTripletValue(self, nums):
        n = len(nums)
        max_val = 0
        
        for j in range(1, n - 1):
            max_i = max(nums[:j])  # best i < j
            for k in range(j + 1, n):
                value = (max_i - nums[j]) * nums[k]
                max_val = max(max_val, value)
        
        return max_val
