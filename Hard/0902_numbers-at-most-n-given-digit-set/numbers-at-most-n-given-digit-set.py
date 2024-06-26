class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # Reference: https://leetcode.com/problems/numbers-at-most-n-given-digit-set/solutions/168279/python-o-logn/
        num = str(n)
        ans = sum(len(digits)**i for i in range(1, len(num)))  # All numbers less than len(num) digits are valid
        for i, c in enumerate(num):  # Deal with all numbers with len(num) digits
            ans += sum(digit < c for digit in digits) * (len(digits)**(len(num) - i - 1))
            if c not in digits:
                break
        else:
            ans += 1
        return ans
