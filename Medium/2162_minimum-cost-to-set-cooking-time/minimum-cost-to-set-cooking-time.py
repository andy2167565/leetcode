class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(m, s):
            if not 99 >= m >= 0 <= s <= 99:
                return float('inf')
            display = str(startAt) + str(100 * m + s)
            moves = sum(display[i] != display[i - 1] for i in range(1, len(display)))
            pushes = len(display) - 1
            return moveCost * moves + pushCost * pushes
        
        mins, secs = divmod(targetSeconds, 60)
        return min(cost(mins, secs), cost(mins - 1, secs + 60))
