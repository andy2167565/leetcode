class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
#======== <Solution 1> ========#
        from fractions import Fraction
        ans = []
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                if Fraction(numerator, denominator).denominator == denominator:
                    ans.append(str(Fraction(numerator, denominator)))
        return ans

#======== <Solution 2> ========#
        ans, values = set(), set()
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                if numerator / denominator not in values:
                    ans.add(f'{numerator}/{denominator}')
                    values.add(numerator / denominator)
        return ans

#======== <Solution 3> ========#
        from math import gcd
        ans = []
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                if gcd(numerator, denominator) == 1:
                    ans.append(f'{numerator}/{denominator}')
        return ans
