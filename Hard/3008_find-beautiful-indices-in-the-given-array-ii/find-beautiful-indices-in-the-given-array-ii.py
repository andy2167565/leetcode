class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # Reference: https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/solutions/4561875/python-kmp-two-pointers-o-n/
        def kmp(s):
            dp = [0] * len(s)
            for i in range(1, len(s)):
                curr = dp[i - 1]
                while curr and s[i] != s[curr]:
                    curr = dp[curr - 1]
                dp[i] = curr + (s[i] == s[curr])
            return dp

        la, lb = len(a), len(b)
        dp1, dp2 = map(kmp, [a + '#' + s, b + '#' + s])
        ii = [i - la * 2 for i, v in enumerate(dp1) if v >= la]
        jj = [j - lb * 2 for j, v in enumerate(dp2) if v >= lb]
        ans = []
        j = 0
        for i in ii:
            while j < len(jj) and jj[j] < i - k:
                j += 1
            if j < len(jj) and jj[j] <= i + k:
                ans.append(i)
        return ans
