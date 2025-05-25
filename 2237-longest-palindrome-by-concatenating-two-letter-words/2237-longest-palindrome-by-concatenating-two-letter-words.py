from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0

        # Use list(count) to avoid RuntimeError
        for word in list(count):
            rev = word[::-1]
            if word != rev and rev in count:
                pairs = min(count[word], count[rev])
                length += pairs * 4
                count[word] -= pairs
                count[rev] -= pairs

        # Handle palindromic words like "cc", "gg"
        for word in list(count):
            if word[0] == word[1]:
                pairs = count[word] // 2
                length += pairs * 4
                count[word] -= pairs * 2

        # Check if one palindromic word can go in the center
        for word in count:
            if word[0] == word[1] and count[word] > 0:
                length += 2
                break

        return length
