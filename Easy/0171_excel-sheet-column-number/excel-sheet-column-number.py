class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
#======== <Solution 1> ========#
        q = 0
        for c in columnTitle:
            q = q * 26 + ord(c) - ord('A') + 1
        return q

#======== <Solution 2> ========#
        def _helper(columnTitle, q):
            if not columnTitle: return q
            return _helper(columnTitle[1:], q * 26 + ord(columnTitle[0]) - ord('A') + 1)
        return _helper(columnTitle, 0)

#======== <Solution 3> ========#
        return sum((ord(c)-ord('A')+1) * 26**(len(columnTitle)-n-1) for n, c in enumerate(columnTitle))
        
#======== <Solution 4> ========#
        return reduce(lambda q, r: q * 26 + r, map(lambda c: ord(c) - ord('A') + 1, columnTitle))
