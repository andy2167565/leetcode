class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
#======== <Solution 1> ========#
        s = [s[1:2], s[2:-1]]
        ans = []
        while s[1]:
            xy_list = [[], []]
            for i, part in enumerate(s):
                for j in range(1, len(part) + 1):
                    cur = part[:j] + '.' + part[j:]
                    if (cur[0] == '0' and len(cur[:j]) > 1) or (cur[-1] == '0' and len(cur[j+1:]) > 0):
                        continue
                    xy_list[i].append(cur.rstrip('.'))
            for x in xy_list[0]:
                for y in xy_list[1]:
                    ans.append(f'({x}, {y})')
            s[0] += s[1][0]
            s[1] = s[1][1:]
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/ambiguous-coordinates/discuss/123851/C%2B%2BJavaPython-Solution-with-Explanation
        import itertools
        def gen(S: str) -> List[str]:
            if not S or (len(S) > 1 and S[0] == S[-1] == '0'):
                return []
            if S[-1] == '0':
                return [S]
            if S[0] == '0':
                return [S[0] + '.' + S[1:]]
            return [S] + [S[:i] + '.' + S[i:] for i in range(1, len(S))]
        s = s[1:-1]
        return [f'({a}, {b})' for i in range(1, len(s)) for a, b in itertools.product(*map(gen, (s[:i], s[i:])))]
