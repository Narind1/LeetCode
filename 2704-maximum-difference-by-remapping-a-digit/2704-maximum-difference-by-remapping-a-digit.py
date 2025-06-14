class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        
        # Function to get all remapped values by changing one digit to new_digit
        def get_all_variations(num_str, new_digit):
            variations = set()
            for d in '0123456789':
                if d == new_digit:
                    continue
                # Replace all occurrences of d with new_digit
                changed = num_str.replace(d, new_digit)
                variations.add(int(changed))
            return variations
        
        # Get all max and min values possible
        max_vals = get_all_variations(num_str, '9')
        min_vals = get_all_variations(num_str, '0')
        
        # Include the original num if no change happens
        max_vals.add(num)
        min_vals.add(num)

        return max(max_vals) - min(min_vals)
