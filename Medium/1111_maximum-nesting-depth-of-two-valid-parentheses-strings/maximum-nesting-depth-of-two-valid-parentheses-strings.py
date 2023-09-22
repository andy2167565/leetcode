class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
# Reference: https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/solutions/358419/confused-by-this-problem-i-was-too-here-is-how-it-became-crystal-clear/
#======== <Solution 1> ========#
        ans, depth = [], 0
        for c in seq:
            if c == '(':
                depth += 1
            ans.append(depth % 2)  # Determined by parity (odd or even) of depth
            if c == ')':
                depth -= 1
        return ans

#======== <Solution 2> ========#
        return [i & 1 ^ (c == '(') for i, c in enumerate(seq)]
