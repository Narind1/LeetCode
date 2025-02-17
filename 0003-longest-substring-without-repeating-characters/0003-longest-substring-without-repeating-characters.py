class Solution:
    def lengthOfLongestSubstring(self, s):
        # Dictionary to store the last seen index of each character.
        char_index = {}
        max_length = 0
        start = 0  # Left pointer for the sliding window
        
        for i, char in enumerate(s):
            # If the character is already in the dictionary and its index is within
            # the current window, move the start pointer to one position after it.
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            # Update the last seen index of the character.
            char_index[char] = i
            # Update the maximum length if the current window is longer.
            max_length = max(max_length, i - start + 1)
        
        return max_length