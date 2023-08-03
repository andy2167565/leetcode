class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Reference: https://leetcode.com/problems/most-profit-assigning-work/solutions/127031/c-java-python-sort-and-two-pointer/
        jobs = sorted(zip(difficulty, profit))
        ans = i = best_profit = 0
        for ability in sorted(worker):  # The minimum best_profit of current worker should be equal to the maximum best_profit of previous workers with less capacities
            while i < len(jobs) and ability >= jobs[i][0]:  # Find the maximum profit that the worker can get
                best_profit = max(best_profit, jobs[i][1])
                i += 1
            ans += best_profit
        return ans
