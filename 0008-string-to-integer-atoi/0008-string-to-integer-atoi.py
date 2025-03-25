class Solution:
    def myAtoi(self, s):
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        i = 0
        if s[0] in ('-', '+'):
            sign = -1 if s[0] == '-' else 1
            i += 1
        
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        num *= sign
        
        int_min, int_max = -2**31, 2**31 - 1
        return max(min(num, int_max), int_min)
