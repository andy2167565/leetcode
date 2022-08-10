class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
#======== <Solution 1> ========#
        return [int(n) for n in str(int("".join(str(i) for i in digits))+1)]

#======== <Solution 2> ========#
        return list(map(int, str(int("".join(map(str, digits)))+1)))

#======== <Solution 3> ========#
        if digits[-1] == 9:
            if len(digits) == 1:
                return [1, 0]
            return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1
        return digits

#======== <Solution 4> ========#
        carry = 1
        for i in reversed(range(len(digits))):
            carry, digits[i] = divmod(digits[i] + carry, 10)
            if carry == 0: return digits
        return [carry] + digits
