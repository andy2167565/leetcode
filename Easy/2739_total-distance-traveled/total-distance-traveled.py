class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
#======== <Solution 1> ========#
        count = 0
        while mainTank >= 5:
            if additionalTank:
                mainTank -= 4
                additionalTank -= 1
            else:
                break
            count += 1
        return (count * 5 + mainTank) * 10

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/total-distance-traveled/solutions/3650469/java-c-python-math-o-1/
        return (mainTank + min((mainTank - 1) // 4, additionalTank)) * 10
