class Solution:
    def can_partition(self, num_str, target, index=0, current_sum=0):
        if index == len(num_str):
            return current_sum == target
        
        for j in range(index + 1, len(num_str) + 1):
            part = int(num_str[index:j])
            if self.can_partition(num_str, target, j, current_sum + part):
                return True
        
        return False

    def punishmentNumber(self, n):
        total = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if self.can_partition(square_str, i):
                total += i * i
        return total

