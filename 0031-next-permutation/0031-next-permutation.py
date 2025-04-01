class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2

        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:  # If there is a pivot
            j = n - 1
            while nums[j] <= nums[i]:  # Find the next larger element
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # Swap

        # Step 3: Reverse the elements after index i
        nums[i + 1:] = reversed(nums[i + 1:])