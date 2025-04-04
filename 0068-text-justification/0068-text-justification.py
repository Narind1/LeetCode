class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, line, line_length = [], [], 0

        for word in words:
            # Check if adding the next word exceeds maxWidth (accounting for spaces)
            if line_length + len(line) + len(word) > maxWidth:
                # Distribute spaces
                for i in range(maxWidth - line_length):
                    line[i % (len(line) - 1 or 1)] += ' '  # Ensure at least 1 word in line
                
                res.append("".join(line))
                line, line_length = [], 0

            line.append(word)
            line_length += len(word)

        # Left-justify the last line
        res.append(" ".join(line).ljust(maxWidth))

        return res
