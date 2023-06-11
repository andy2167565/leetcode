class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
#======== <Solution 1> ========#
        ans = 1
        l = pair = 0
        for r in range(1, len(s)):
            if s[r - 1] == s[r]:
                l, pair = pair, r
            ans = max(ans, r - l + 1)
        return ans

#======== <Solution 2> ========#
        # Reference with my comment: https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/solutions/3622357/explained-simple-and-clear-python3-code/
        lengths = [1]
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:  # Start counting new length if a pair exists
                lengths.append(1)
            else:
                lengths[-1] += 1
        return max((lengths[j - 1] + lengths[j] for j in range(1, len(lengths))), default=lengths[0])

#======== <Solution 3> ========#
        s = s[0] + s + s[-1]
        pairs = [i for i in range(len(s) - 1) if s[i] == s[i + 1]]
        return max((y - x for x, y in zip(pairs, pairs[2:])), default=len(s) - 2)
