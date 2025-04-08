class Solution(object):
    def minimumOperations(self, nums):
        operations = 0
        while len(nums) > 0:
            # Check if the array has only unique elements
            if len(set(nums)) == len(nums):
                break
            # Remove first 3 elements (or less if fewer)
            nums = nums[3:]
            operations += 1
        return operations
        