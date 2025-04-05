class Solution:
    def subsetXORSum(self, nums):
        self.total = 0

        def dfs(i, current_xor):
            if i == len(nums):
                self.total += current_xor
                return
            # Include nums[i]
            dfs(i + 1, current_xor ^ nums[i])
            # Exclude nums[i]
            dfs(i + 1, current_xor)

        dfs(0, 0)
        return self.total
