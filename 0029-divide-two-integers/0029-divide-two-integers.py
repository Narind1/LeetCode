class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1 

        negative = (dividend < 0) ^ (divisor < 0)  # XOR to check if signs differ
        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):  # Doubling divisor
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient
