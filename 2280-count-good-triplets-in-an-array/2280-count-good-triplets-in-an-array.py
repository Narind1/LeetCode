class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)
    
    def update(self, index, value):
        index += 1  # 1-based indexing
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index
    
    def query(self, index):
        index += 1
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos = [0] * n
        for i, num in enumerate(nums2):
            pos[num] = i
        
        A = [pos[num] for num in nums1]
        
        left_tree = FenwickTree(n)
        left_count = [0] * n
        for i in range(n):
            left_count[i] = left_tree.query(A[i] - 1)
            left_tree.update(A[i], 1)
        
        right_tree = FenwickTree(n)
        right_count = [0] * n
        for i in range(n - 1, -1, -1):
            right_count[i] = right_tree.query(n - 1) - right_tree.query(A[i])
            right_tree.update(A[i], 1)
        
        ans = 0
        for i in range(n):
            ans += left_count[i] * right_count[i]
        
        return ans
