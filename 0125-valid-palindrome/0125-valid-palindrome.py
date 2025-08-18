class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # keep only alphanumeric, make lowercase
        cleaned = [ch.lower() for ch in s if ch.isalnum()]

        i, j = 0, len(cleaned) - 1

        while i < j:
            if cleaned[i] != cleaned[j]:
                return False
            i += 1
            j -= 1

        return True
