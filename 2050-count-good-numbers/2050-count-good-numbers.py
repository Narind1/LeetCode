class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        def power(x, y):
            result = 1
            x %= MOD
            while y > 0:
                if y % 2 == 1:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                y //= 2
            return result
        
        even_count = (n + 1) // 2
        odd_count = n // 2
        return (power(5, even_count) * power(4, odd_count)) % MOD

