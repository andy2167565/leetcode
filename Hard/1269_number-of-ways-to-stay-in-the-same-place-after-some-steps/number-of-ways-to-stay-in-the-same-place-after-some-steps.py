class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # Reference: https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/solutions/4169623/video-give-me-10-minutes-how-we-think-abou-a-solution-python-javascript-java-c/
        max_position = min(steps // 2 + 1, arrLen)
        curr_ways, next_ways = [0] * (max_position + 2), [0] * (max_position + 2)
        curr_ways[1] = 1  # Consider index 1 as the starting point
        for _ in range(steps):
            for pos in range(1, max_position + 1):  # Index 0 and -1 are extra positions to prevent from out-of-bound error
                next_ways[pos] = (curr_ways[pos] + curr_ways[pos - 1] + curr_ways[pos + 1]) % (10**9 + 7)
            curr_ways, next_ways = next_ways, curr_ways  # next_ways is the next curr_ways
        return curr_ways[1]
