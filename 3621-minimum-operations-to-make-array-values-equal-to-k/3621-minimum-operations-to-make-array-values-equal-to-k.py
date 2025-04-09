class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Step 1: If any number < k, impossible
        if any(num < k for num in nums):
            return -1
        
        # Step 2: Only care about unique values > k
        higher_values = set([num for num in nums if num > k])
        
        return len(higher_values)
