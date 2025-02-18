class Solution:
    def romanToInt(self, s):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        prev_value = 0

        for char in reversed(s):  # Process from right to left
            curr_value = roman_dict[char]
            if curr_value < prev_value:  # If smaller value precedes larger, subtract it
                num -= curr_value
            else:
                num += curr_value
            prev_value = curr_value
        
        return num