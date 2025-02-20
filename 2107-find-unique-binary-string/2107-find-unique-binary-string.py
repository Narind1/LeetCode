class Solution(object):
    def findDifferentBinaryString(self, nums):
        length = len(nums[0])
        b = []

        for i in range(2**length - 1, -1, -1):
            binary_str = bin(i)[2:].zfill(length)
            b.append(binary_str)

        b = [x for x in b if x not in nums]
        return b[0]    