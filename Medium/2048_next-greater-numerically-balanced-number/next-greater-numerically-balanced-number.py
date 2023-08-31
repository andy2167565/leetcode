class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        import itertools, bisect
        base, candidates = ['1', '22', '122', '333', '1333', '4444', '44441', '55555', '22333', '122333', '155555', '224444', '666666'], []
        for s in base:
            candidates += list(set(int(''.join(perm)) for perm in itertools.permutations(list(s))))
        candidates.append(1224444)
        candidates.sort()
        return candidates[bisect.bisect_right(candidates, n)]
