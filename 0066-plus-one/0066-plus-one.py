class Solution(object):
    def plusOne( self,digits):
        n = len(digits)
        digits[-1] += 1  
        for i in range(n - 1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                if i > 0:
                    digits[i - 1] += 1
                else:
                    digits.insert(0, 1)  
        return digits