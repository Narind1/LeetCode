from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        total = 0
        result = 0

        for right in range(len(nums)):
            total += nums[right]
            while total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            result += (right - left + 1)

        return result
