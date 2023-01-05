class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/longest-repeating-character-replacement/solutions/765776/python-two-pointers-process-for-coding-interviews/
        import collections
        l, ans, freq = 0, 0, collections.defaultdict(int)
        for r in range(len(s)):
            freq[s[r]] += 1
            window = r - l + 1  # Number of chars between left and right
            if window - max(freq.values()) <= k:  # Replacement cost = window - highest frequency
                ans = max(ans, window)
            else:  # Move the window 1 step forward
                freq[s[l]] -= 1
                l += 1
        return ans

#======== <Solution 2> ========#
        ans, max_freq, freq = 0, 0, {}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            max_freq = max(max_freq, freq[s[i]])
            if ans - max_freq < k:
                ans += 1
            else:  # ans = max_freq + k
                freq[s[i - ans]] -= 1
        return ans

#======== <Solution 3> ========#
        import collections
        l, freq = 0, collections.Counter()
        for r in range(len(s)):
            freq[s[r]] += 1
            if r - l + 1 > freq.most_common(1)[0][1] + k:
                freq[s[l]] -= 1
                l += 1
        return len(s) - l
