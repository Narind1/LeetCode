class Solution(object):
    def reverse(self, n):  # Added 'self' to define it as a method
        if n < 0:
            sign = -1
        else:
            sign = 1  # Check for negative numbers
        rev = int(str(abs(n))[::-1])  # Reverse the number as a string
        if rev > 2**31 - 1:
                return 0
        return sign * rev