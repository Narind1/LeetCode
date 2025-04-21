class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        curr_sum = 0
        min_sum = 0
        max_sum = 0

        for diff in differences:
            curr_sum += diff
            min_sum = min(min_sum, curr_sum)
            max_sum = max(max_sum, curr_sum)

        left = lower - min_sum
        right = upper - max_sum

        return max(0, right - left + 1)