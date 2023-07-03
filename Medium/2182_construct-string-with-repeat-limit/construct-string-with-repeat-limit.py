class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        import collections
        ans, candidates = '', sorted([ch, count] for ch, count in collections.Counter(s).items())
        while candidates:
            ch, count = candidates.pop()
            ans += ch * min(count, repeatLimit)
            if candidates and count > repeatLimit:
                ans += candidates[-1][0]
                candidates[-1][1] -= 1
                if not candidates[-1][1]:
                    candidates.pop()
                candidates.append([ch, count - repeatLimit])
        return ans
