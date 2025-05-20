from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        
        # Mark ranges in diff array
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1

        # Build prefix sum to count touches for each index
        count = [0] * n
        current = 0
        for i in range(n):
            current += diff[i]
            count[i] = current

        # Compare count[i] with nums[i]
        for i in range(n):
            if nums[i] > count[i]:
                return False

        return True
