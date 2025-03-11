class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Place each number in its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # Swap
            
        # Find the first missing number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
        