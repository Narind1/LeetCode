class Solution:
    def inorderTraversal(self, root):
        stack = []
        result = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left  # Move left

            current = stack.pop()  # Visit node
            result.append(current.val)
            current = current.right  # Move right

        return result
