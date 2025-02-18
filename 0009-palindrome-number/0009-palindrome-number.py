class Solution:
    def isPalindrome(self, x):
        if x >= 0:
            rev = int(str(x)[::-1])
            if x == rev:
                return True
            else:
                return False
        else:
            return False
