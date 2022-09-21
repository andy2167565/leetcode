class Solution:
    def secondHighest(self, s: str) -> int:
#======== <Solution 1> ========#
        digit = sorted(int(c) for c in set(s) if c.isdigit())
        return digit[-2] if len(digit) > 1 else -1

#======== <Solution 2> ========#
        import re
        digit = sorted(set(map(int, re.findall(r'\d', s))))
        return digit[-2] if len(digit) > 1 else -1

#======== <Solution 3> ========#
        return ([-1, -1] + sorted(map(int, filter(lambda c: c.isdigit(), set(s)))))[-2]

#======== <Solution 4> ========#
        first = second = -1
        for c in set(s):
            if c.isdigit():
                second = max(min(first, int(c)), second)
                first = max(first, int(c))
        return second
