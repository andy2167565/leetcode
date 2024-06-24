class Solution:
    def distinctSubseqII(self, s: str) -> int:
# Reference: https://leetcode.com/problems/distinct-subsequences-ii/solutions/192017/java-c-python-dp-4-lines-o-n-time-o-1-space/
#======== <Solution 1> ========#
        end = [0] * 26  # end[i]: The number of subsequences that ends with i-th character
        for c in s:
            end[ord(c) - ord('a')] = sum(end) + 1  # Append to all existing subsequences and include the character itself
        return sum(end) % (10**9 + 7)

#======== <Solution 2> ========#
        import collections
        ans, end = 0, collections.Counter()
        for c in s:
            ans, end[c] = ans * 2 + 1 - end[c], ans + 1
        return ans % (10**9 + 7)
