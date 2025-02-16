class Solution:
    def constructDistancedSequence(self, n):
        sequence = [0] * (2 * n - 1)  # Initialize an empty sequence
        used = set()  # Track placed numbers

        def backtrack(index):
            if index == len(sequence):
                return True  # Successfully placed all numbers

            if sequence[index] != 0:  # Skip filled positions
                return backtrack(index + 1)

            for num in range(n, 0, -1):  # Try placing numbers from largest to smallest
                if num in used:
                    continue

                j = index + num if num > 1 else index  # Compute second position
                if j < len(sequence) and sequence[j] == 0:
                    sequence[index], sequence[j] = num, num  # Place the number
                    used.add(num)  # Mark as used

                    if backtrack(index + 1):
                        return True  # If sequence is valid, return success

                    sequence[index], sequence[j] = 0, 0  # Backtrack
                    used.remove(num)

            return False  # No valid placement found

        backtrack(0)  # Start backtracking from index 0
        return sequence

