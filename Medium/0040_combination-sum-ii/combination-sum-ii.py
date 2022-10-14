class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/combination-sum-ii/discuss/16870/DP-solution-in-Python/16693
        # Use tuple and set to prevent duplicate combinations e.g. [1, 7] & [7, 1], [1, 2, 5] & [2, 1, 5]
        dp = [{tuple()}] + [set() for _ in range(target)]
        for num in sorted(candidates):  # Sort candidates to align each set of same combinations e.g. [7, 1] -> [1, 7], [2, 1, 5] -> [1, 2, 5]
            for i in reversed(range(num, target + 1)):  # Reverse the index list to avoid one element used more than once
                dp[i] |= {sub + (num,) for sub in dp[i - num]}
        return list(map(list, dp[-1]))

#======== <Solution 2> ========#
        # Reference 1: https://leetcode.com/problems/combination-sum-ii/discuss/17020/Python-easy-to-understand-backtracking-solution/1385491
        # Reference 2: https://leetcode.com/problems/combination-sum-ii/discuss/16944/Beating-98-Python-solution-using-recursion-with-comments/675085
        # Reference 3: https://leetcode.com/problems/combination-sum-ii/discuss/750378/Python3-DFS-solutionstemplates-to-6-different-classic-backtracking-problems-and-more
        candidates.sort()
        ans = []
        def dfs(target, index, path):
            if target < 0:  # Current sum is larger than target
                return
            if not target:  # Current sum equals to target
                ans.append(path)
                return
            for i in range(index, len(candidates)):
                # candidates[i] == candidates[i - 1]: Avoid duplicate combinations among different rounds
                # e.g. candidates = [10, 1a, 2, 7, 6, 1b, 5] -> [1a, 1b, 2, 5, 6, 7, 10], target = 8
                # We will have [1a, 2, 5] in the first round and [1b, 2, 5] in the second round, which are basically the same
                # Therefore we discard [1b, 2, 5] after the first round
                
                # Using i > index instead of i >= index is to include duplicate elements in the first round
                # According to the example above, one of the combinations is [1a, 1b, 6]. If we set i >= index, this combination will be discarded when it reaches 1b since 1a == 1b
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                dfs(target - candidates[i], i + 1, path + [candidates[i]])  # Change the start to i + 1 because one element can only be used once
        dfs(target, 0, [])
        return ans
