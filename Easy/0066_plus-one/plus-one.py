class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
#======== <Solution 1> ========#
        num = int("".join(str(i) for i in digits))
        if num == 0:
            digits[-1] = 1
            return digits
        else:
            return str(num+1)
        
#======== <Solution 2> ========#
        return str(int("".join(str(i) for i in digits))+1).zfill(len(digits))
