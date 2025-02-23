class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        # Mapping of digits to letters, like on a phone keypad
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))  # Join letters to form a string
                return
            
            for letter in phone_map[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()  # Remove last letter to backtrack
        
        backtrack(0, [])
        return result
