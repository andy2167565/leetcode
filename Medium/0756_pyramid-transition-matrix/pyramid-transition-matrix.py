class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        import collections, itertools
        pool = collections.defaultdict(list)
        for s in allowed:
            pool[s[:2]].append(s[-1])

        def dfs(bottom):
            if len(bottom) == 1:
                return True
            for level in itertools.product(*(pool[x + y] for x, y in zip(bottom[:-1], bottom[1:]))):  # Iterate through each possible combination of the level
                if dfs(level):
                    return True
            return False

        return dfs(bottom)
