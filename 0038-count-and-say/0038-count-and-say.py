class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        s = "1"
        
        for _ in range(n - 1):
            next_s = ""
            i = 0
            
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:  # Count consecutive same digits
                    count += 1
                    i += 1
                
                next_s += str(count) + s[i]  # Append count and digit
                i += 1
            
            s = next_s  # Move to the next sequence
        
        return s
