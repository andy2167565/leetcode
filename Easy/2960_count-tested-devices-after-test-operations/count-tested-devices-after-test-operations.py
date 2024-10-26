class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for num in batteryPercentages:
            ans += num > ans
        return ans
