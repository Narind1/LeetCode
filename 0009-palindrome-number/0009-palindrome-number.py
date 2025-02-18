class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        rev = int(str(x)[::-1])
        return x == rev