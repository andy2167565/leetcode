class Solution:
    def minimumDeletions(self, s: str) -> int:
#======== <Solution 1> ========#
        ans, stack = 0, []
        for c in s:
            if stack and stack[-1] == 'b' and c == 'a':
                stack.pop()
                ans += 1
            else:
                stack.append(c)
        return ans

#======== <Solution 2> ========#
        a, b, ans = s.count('a'), 0, len(s)
        for c in s:  # Count the total occurrences of 'a' on the right and 'b' on the left for each index
            if c == 'b':
                ans = min(ans, a + b)
                b += 1
            else:
                a -= 1
        return min(ans, b)

#======== <Solution 3> ========#
        ans = suffix = 0
        for c in reversed(s):
            if c == 'a':
                suffix += 1
            else:
                ans = min(ans + 1, suffix)
        return ans
