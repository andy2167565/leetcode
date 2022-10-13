class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/combination-sum/discuss/937255/Python-3-or-DFSBacktracking-and-Two-DP-methods-or-Explanations
        dp = [[[]]] + [[] for _ in range(target)]
        for num in candidates:
            for i in range(num, target + 1):
                dp[i] += [sub + [num] for sub in dp[i - num]]
        return dp[-1]

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/combination-sum/discuss/429538/General-Backtracking-questions-solutions-in-Python-for-reference-%3A
        ans = []
        def dfs(target, index, path):
            if target < 0:  # Current sum is larger than target
                return
            if not target:  # Current sum equals to target
                ans.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(target - candidates[i], i, path + [candidates[i]])
        dfs(target, 0, [])
        return ans
