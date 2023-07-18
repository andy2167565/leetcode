class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # Reference: https://leetcode.com/problems/consecutive-numbers-sum/solutions/128959/java-python-3-5-liners-o-n-0-5-math-method-w-explanation-and-analysis/
        i, ans = 1, 0
        while n > i * (i - 1) // 2:
            if not (n - i * (i - 1) // 2) % i:
                ans += 1
            i += 1
        return ans
