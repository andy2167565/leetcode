class Solution:
    def countBinarySubstrings(self, s: str) -> int:
#======== <Solution 1> ========#
        import itertools
        count = [list(g[1]).count(g[0]) for g in itertools.groupby(s)]
        return sum(min(i) for i in zip(count, count[1:]))

#======== <Solution 2> ========#
        count = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(i) for i in zip(count, count[1:]))

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/count-binary-substrings/discuss/1172569/Short-and-Easy-w-Explanation-and-Comments-or-Keeping-Consecutive-0s-and-1s-Count-or-Beats-100
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ans += min(prev, cur)
                prev, cur = cur, 0
            cur += 1
        return ans + min(prev, cur)

# Reference: https://leetcode.com/problems/count-binary-substrings/discuss/108626/Python-intuitive-approaches-with-explanation-(3-liner)
#======== <Solution 4> ========#
        flips = [0] + [i for i in range(1, len(s)) if s[i] != s[i - 1]] + [len(s)]
        chunks = [i[1] - i[0] for i in zip(flips, flips[1:])]
        return sum(min(i) for i in zip(chunks, chunks[1:]))

#======== <Solution 5> ========#
        count, ans = [1], 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                count.append(0)
            count[-1] += 1
        return sum(min(i) for i in zip(count, count[1:]))

#======== <Solution 6> ========#
        # Reference: https://leetcode.com/problems/count-binary-substrings/discuss/108604/1-liners
        return sum(min(map(len, pair)) for pair in re.findall('(0+|1+)(?=(0+|1*))', s))
