class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
# Reference: https://leetcode.com/problems/maximum-points-in-an-archery-competition/solutions/1865571/c-python-3-solutions-top-down-dp-backtracking-bit-masking-clean-concise/
#======== <Solution 1> ========#
        import functools

        @functools.cache
        def dp(k, numArrows):
            if k == 12 or numArrows <= 0:
                return 0
            maxScore = dp(k + 1, numArrows)  # Bob loses
            if numArrows > aliceArrows[k]:
                maxScore = max(maxScore, dp(k + 1, numArrows - aliceArrows[k] - 1) + k)  # Bob wins
            return maxScore
        
        ans, remainBobArrows = [0] * 12, numArrows
        for k in range(12):  # Backtracking
            if dp(k, numArrows) != dp(k + 1, numArrows):  # Bob wins
                ans[k] = aliceArrows[k] + 1
                numArrows -= ans[k]
                remainBobArrows -= ans[k]
        ans[0] += remainBobArrows  # Distribute the remaining arrows to any section, which is simply the first section here
        return ans

#======== <Solution 2> ========#
        self.bestScore = 0
        self.bestBobArrows = None
        
        def backtracking(k, remainArrows, score, bobArrows):
            if k == 12:
                if score > self.bestScore:
                    self.bestScore = score
                    self.bestBobArrows = bobArrows[::]
                return
            backtracking(k + 1, remainArrows, score, bobArrows)  # Bob loses
            
            # Bob wins
            arrowsNeeded = aliceArrows[k] + 1
            if remainArrows >= arrowsNeeded:
                old = bobArrows[k]
                bobArrows[k] = arrowsNeeded  # Set new
                backtracking(k + 1, remainArrows - arrowsNeeded, score + k, bobArrows)
                bobArrows[k] = old  # Backtrack
        
        backtracking(0, numArrows, 0, [0] * 12)
        self.bestBobArrows[0] += numArrows - sum(self.bestBobArrows)  # Distribute the remaining arrows to any section, which is simply the first section here
        return self.bestBobArrows

#======== <Solution 3> ========#
        def test(mask, remainArrows):
            score, bobArrows = 0, [0] * 12
            for k in range(12):
                if (mask >> k) & 1:
                    arrowsNeeded = aliceArrows[k] + 1
                    if remainArrows < arrowsNeeded:
                        return 0, []
                    score += k
                    bobArrows[k] = arrowsNeeded
                    remainArrows -= arrowsNeeded
            bobArrows[0] += remainArrows  # Distribute the remaining arrows to any section, which is simply the first section here
            return score, bobArrows
        
        bestScore, bestBobArrows = 0, None
        for mask in range(1 << 12):
            score, bobArrows = test(mask, numArrows)
            if score > bestScore:
                bestScore, bestBobArrows = score, bobArrows
        return bestBobArrows
