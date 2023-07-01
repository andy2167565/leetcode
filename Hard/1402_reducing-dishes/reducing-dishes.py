class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
#======== <Solution 1> ========#
        ans = curr_sum = 0
        satisfaction.sort()  # Start from the most satisfied dish
        while satisfaction and satisfaction[-1] + curr_sum > 0:  # Total satisfaction will increase by serving the next dish
            curr_sum += satisfaction.pop()
            ans += curr_sum
        return ans

#======== <Solution 2> ========#
        import itertools
        return max(itertools.accumulate(itertools.accumulate(sorted(satisfaction, reverse=True), initial=0)))
