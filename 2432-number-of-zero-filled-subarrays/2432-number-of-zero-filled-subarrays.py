class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        count=0

        for num in nums:
            if num==0:
                j+=1
                count+=j
            else:
                j=0
        return count