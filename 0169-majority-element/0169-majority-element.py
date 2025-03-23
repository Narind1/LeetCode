from collections import Counter

class Solution:
    def majorityElement(self, nums):
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)
