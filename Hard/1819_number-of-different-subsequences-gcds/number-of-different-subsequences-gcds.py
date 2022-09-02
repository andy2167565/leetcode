class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        # Reference 1 (Code): https://leetcode.com/problems/number-of-different-subsequences-gcds/discuss/1141361/Python-Python-2-solutions-%2B-2liner-explained
        # Reference 2 (Explanation): https://leetcode.com/problems/number-of-different-subsequences-gcds/discuss/1141547/Python-Test-every-GCD-(proof)-O(M-log-M)
        # Reference 3 (Explanation): https://leetcode.com/problems/number-of-different-subsequences-gcds/discuss/1142846/C%2B%2B-with-explanation-or-Simple-Solution
        import math
        M, nums, ans = max(nums), set(nums), 0
        for div in range(1, M + 1):
            g = 0
            for multi_div in range(div, M + 1, div):
                if multi_div in nums:
                    g = math.gcd(g, multi_div)
                    if g == div:
                        ans += 1
                        break
        return ans
