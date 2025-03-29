class Solution(object):
    def sum_of_squares(self, n):
        return sum(int(digit) ** 2 for digit in str(n))

    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sum_of_squares(n)
        return n == 1