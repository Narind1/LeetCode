class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n):
        if n <= 2:
            return n
        if n not in self.memo:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]
