class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # Reference: https://leetcode.com/problems/broken-calculator/solutions/234484/java-c-python-change-y-to-x-in-1-line/
#======== <Solution 1> ========#
        multiple = 0
        while startValue < target:
            multiple += target % 2 + 1
            target = (target + 1) // 2
        return multiple + startValue - target

#======== <Solution 2> ========#
        return startValue - target if startValue >= target else 1 + target % 2 + self.brokenCalc(startValue, (target + 1) // 2)

#======== <Solution 3> ========#
        ans, multiple = 0, 1
        while startValue * multiple < target:
            multiple *= 2
            ans += 1
        diff = startValue * multiple - target
        while diff:
            ans += diff // multiple
            diff -= diff // multiple * multiple
            multiple //= 2
        return ans
