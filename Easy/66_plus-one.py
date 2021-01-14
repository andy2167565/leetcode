class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
#======== <Solution 1> ========#
        num = int("".join(str(i) for i in digits))
        if num == 0:
            digits[-1] = 1
            return digits
        else:
            return str(num+1)
        
#======== <Solution 2> ========#
        return str(int("".join(str(i) for i in digits))+1).zfill(len(digits))
