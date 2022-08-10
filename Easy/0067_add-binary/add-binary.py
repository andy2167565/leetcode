class Solution:
    def addBinary(self, a: str, b: str) -> str:
#======== <Solution 1> ========#
        return bin(int(a, 2) + int(b, 2))[2:]
        
#======== <Solution 2> ========#
        a_len = len(a)
        b_len = len(b)
        carry = 0
        bin_sum = ""
        # Sum corresponding digits in two numbers
        while a_len > 0 or b_len > 0:
            # digit_sum is set as the carry from previous round
            digit_sum = carry
            if b_len > 0:
                digit_sum += int(b[b_len-1])
                b_len -= 1
            if a_len > 0:
                digit_sum += int(a[a_len-1])
                a_len -= 1
            bin_sum = ''.join((str(digit_sum % 2), bin_sum))
            carry = int(digit_sum / 2)
        if carry != 0:
            bin_sum = ''.join((str(carry), bin_sum))
        return bin_sum
