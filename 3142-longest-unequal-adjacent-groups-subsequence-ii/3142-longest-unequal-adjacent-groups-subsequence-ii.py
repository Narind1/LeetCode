from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hamming(s1, s2):
            return sum(c1 != c2 for c1, c2 in zip(s1, s2))
        
        n = len(words)
        dp = [1] * n       # dp[i] = length of longest valid subsequence ending at i
        parent = [-1] * n  # used to reconstruct the path

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and hamming(words[i], words[j]) == 1:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
        
        # Find the index of the last word in the longest subsequence
        max_index = max(range(n), key=lambda i: dp[i])
        
        # Reconstruct the subsequence
        result = []
        while max_index != -1:
            result.append(words[max_index])
            max_index = parent[max_index]
        
        return result[::-1]
