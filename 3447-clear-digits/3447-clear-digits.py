class Solution(object):
    def clearDigits(self, s):
        stack = []
    
        for ch in s:
            if ch.isdigit():
                # Remove the closest non-digit character to its left if it exists
                while stack and stack[-1].isdigit():
                    stack.pop()  # Ensure we remove a non-digit
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)