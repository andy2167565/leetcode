class Solution:
    def numTilings(self, n: int) -> int:
        # Reference: https://leetcode.com/problems/domino-and-tromino-tiling/solutions/1620975/c-python-simple-solution-w-images-explanation-optimization-from-brute-force-to-dp/
        import functools
        @functools.cache
        def solve(i, previous_gap):
            if i > n:
                return 0
            if i == n:
                return not previous_gap
            if previous_gap:
                return solve(i + 1, False) + solve(i + 1, True)
            return solve(i + 1, False) + solve(i + 2, False) + 2 * solve(i + 2, True)
        return solve(0, False) % (10**9 + 7)
