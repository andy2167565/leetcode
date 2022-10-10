class Solution:
    def countBits(self, n: int) -> List[int]:
#======== <Solution 1> ========#
        return [sum(map(int, bin(i)[2:])) for i in range(n + 1)]

#======== <Solution 2> ========#
        return [bin(i).count('1') for i in range(n + 1)]

#======== <Solution 3> ========#
        ans = []
        for i in range(n + 1):
            count = 0
            while i:
                i, r = divmod(i, 2)
                count += r
            ans.append(count)
        return ans

#======== <Solution 4> ========#
        # Reference: https://leetcode.com/problems/counting-bits/discuss/656849/Python-Simple-Solution-with-Clear-Explanation
        dp = [0]
        for i in range(1, n + 1):
            dp.append(dp[i >> 1] + i % 2)
        return dp

#======== <Solution 5> ========#
        # Reference: https://leetcode.com/problems/counting-bits/discuss/79538/Simple-Python-Solution/742084
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp
