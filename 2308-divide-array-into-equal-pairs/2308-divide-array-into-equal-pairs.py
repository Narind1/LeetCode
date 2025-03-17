class Solution(object):
    def divideArray(self, nums):
        count = Counter(nums)
        return all(v % 2 == 0 for v in count.values())