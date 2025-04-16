from collections import defaultdict

class Solution:
    def countGood(self, nums, k):
        left = 0
        total = 0
        count = defaultdict(int)
        pairs = 0

        for right in range(len(nums)):
            val = nums[right]
            pairs += count[val]  # add the number of existing identical elements
            count[val] += 1

            while pairs >= k:
                total += len(nums) - right
                count[nums[left]] -= 1
                pairs -= count[nums[left]]
                left += 1

        return total
