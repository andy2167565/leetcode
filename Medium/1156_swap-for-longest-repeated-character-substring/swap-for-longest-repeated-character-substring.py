class Solution:
    def maxRepOpt1(self, text: str) -> int:
        import itertools, collections
        groups = [[c, len(list(g))] for c, g in itertools.groupby(text)]
        counter = collections.Counter(text)
        ans = max(min(l + 1, counter[c]) for c, l in groups)  # Extend the group by 1 and use min in case that there's no extra character to extend
        for i in range(1, len(groups) - 1):
            if groups[i - 1][0] == groups[i + 1][0] and groups[i][1] == 1:  # Merge 2 adjacent groups together which are separated by only 1 character
                ans = max(ans, min(groups[i - 1][1] + groups[i + 1][1] + 1, counter[groups[i + 1][0]]))
        return ans
