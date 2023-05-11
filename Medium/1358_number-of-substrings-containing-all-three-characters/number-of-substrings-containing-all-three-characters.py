class Solution:
    def numberOfSubstrings(self, s: str) -> int:
# Reference: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/solutions/516977/java-c-python-easy-and-concise/
#======== <Solution 1> ========#
        ans = l = 0
        count = {c: 0 for c in 'abc'}
        for r in range(len(s)):
            count[s[r]] += 1
            while all(count.values()):  # Current window includes all three characters
                count[s[l]] -= 1
                l += 1
            ans += l  # All substrings that includes characters before index l are valid
        return ans

#======== <Solution 2> ========#
        ans, last = 0, [-1] * 3  # last stores the index of last occurrence for each character
        for i, c in enumerate(s):
            last[ord(c) - 97] = i
            ans += 1 + min(last)  # min(last) is the left pointer of current window
        return ans
