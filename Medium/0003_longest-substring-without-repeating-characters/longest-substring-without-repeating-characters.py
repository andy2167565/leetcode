class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#======== <Solution 1> ========#
        l = r = ans = 0
        while r < len(s):
            while len(set(s[l: r + 1])) < len(s[l: r + 1]):
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation
        start = ans = 0
        seen = {}  # Store the last seen index for each character
        for i, c in enumerate(s):
            if c in seen and start <= seen[c]:
                start = seen[c] + 1
            else:
                ans = max(ans, i - start + 1)
            seen[c] = i
        return ans
