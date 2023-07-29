class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
#======== <Solution 1> ========#
        if not time:
            return list(range(len(security)))
        n = len(security)
        left, right = [0] * n, [0] * n
        for i in range(1, n):
            if security[i - 1] >= security[i]:  # Build non-increasing on the left side (inclusive)
                left[i] = left[i - 1] + 1
            if security[~i] <= security[~i + 1]:  # Build non-decreasing on the right side (inclusive)
                right[~i] = right[~i + 1] + 1
        return [i for i in range(n) if left[i] >= time and right[i] >= time]

#======== <Solution 2> ========#
        import functools
        n = len(security)
        @functools.cache
        def dfs(i, dr):
            return dfs(i + dr, dr) + 1 if 0 <= i + dr < n and security[i] <= security[i + dr] else 0
        return [i for i in range(n) if dfs(i, -1) >= time and dfs(i, 1) >= time]
