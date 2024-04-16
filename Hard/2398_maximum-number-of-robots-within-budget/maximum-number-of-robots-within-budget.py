class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        # Reference: https://leetcode.com/problems/maximum-number-of-robots-within-budget/solutions/2524838/java-c-python-sliding-window-o-n-solution/
        import collections
        curr_cost = i = 0
        time_desc = collections.deque()  # time_desc[0] is the current maximum charge time in sliding window
        for j in range(len(chargeTimes)):
            curr_cost += runningCosts[j]
            while time_desc and chargeTimes[time_desc[-1]] <= chargeTimes[j]:
                time_desc.pop()
            time_desc.append(j)
            if chargeTimes[time_desc[0]] + (j - i + 1) * curr_cost > budget:  # The cost of current sliding window has exceeded budget
                if time_desc[0] == i:
                    time_desc.popleft()
                curr_cost -= runningCosts[i]
                i += 1
        return len(chargeTimes) - i
