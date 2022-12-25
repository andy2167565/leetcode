class Solution:
    def captureForts(self, forts: List[int]) -> int:
#======== <Solution 1> ========#
        def attack(forts):
            ans, captured = 0, -1
            for f in forts:
                if f == 1:
                    captured = 0
                elif not f:
                    captured += captured >= 0
                else:
                    ans, captured = max(ans, captured), -1
            return ans
        return max(attack(forts), attack(forts[::-1]))

#======== <Solution 2> ========#
        ans = start = 0
        for i, f in enumerate(forts):
            if f:
                if forts[start] == -f:  # Fort with opposite sign compared to start
                    ans = max(ans, i - start - 1)
                start = i
        return ans

#======== <Solution 3> ========#
        import itertools
        group, ans = [(f, len(list(g))) for f, g in itertools.groupby(forts)], 0
        for i in range(1, len(group) - 1):
            if group[i - 1][0] * group[i + 1][0] == -1:  # Group combinations: (1, 0, -1) or (-1, 0, 1)
                ans = max(ans, group[i][1])  # Update number of 0's in the middle
        return ans
