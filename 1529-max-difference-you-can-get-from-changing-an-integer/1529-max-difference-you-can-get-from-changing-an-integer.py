class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        
        # For max number: replace first digit that's not 9 with 9
        for d in num_str:
            if d != '9':
                max_num = int(num_str.replace(d, '9'))
                break
        else:
            max_num = num  # all digits are 9 already
        
        # For min number: if first digit is not 1, replace it with 1
        if num_str[0] != '1':
            min_num = int(num_str.replace(num_str[0], '1'))
        else:
            # first digit is 1, replace next digit that is not 0 or 1 with 0
            for d in num_str[1:]:
                if d != '0' and d != '1':
                    min_num = int(num_str.replace(d, '0'))
                    break
            else:
                min_num = num  # already minimal
        
        return max_num - min_num
