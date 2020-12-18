class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed_num = int(''.join([i for i in reversed(list(str(abs(x))))]))
        reversed_num = -reversed_num if x < 0 else reversed_num
        return reversed_num if -pow(2, 31) <= reversed_num <= pow(2, 31)-1 else 0
