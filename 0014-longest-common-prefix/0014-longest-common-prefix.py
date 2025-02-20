class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        strs.sort()
        first, last = strs[0], strs[-1]

        prefix = ""
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                prefix += first[i]
            else:
                break

        return prefix
        