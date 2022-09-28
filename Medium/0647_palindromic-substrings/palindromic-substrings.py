class Solution:
    def countSubstrings(self, s: str) -> int:
#======== <Solution 1> ========#
        ans = center_left = center_right = 0
        while center_right < len(s):
            cur_left, cur_right = center_left, center_right
            while cur_left >= 0 and cur_right < len(s) and s[cur_left] == s[cur_right]:
                ans += 1
                cur_left -= 1
                cur_right += 1
            if center_left == center_right:
                center_right += 1  # even case, like "abba"
            else:
                center_left += 1  # odd case, like "aba"
        return ans

#======== <Solution 2> ========#
        ans = 0
        for i in range(len(s)):
            for left, right in [(i, i), (i, i + 1)]:
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    ans += 1
                    left -= 1
                    right += 1
        return ans

#======== <Solution 3> ========#
        # Reference 1: https://leetcode.com/problems/longest-palindromic-substring/discuss/3337/Manacher-algorithm-in-Python-O(n)
        # Reference 2: https://www.youtube.com/watch?v=YVZttWzvyw8&ab_channel=FluentAlgorithms
        # Reference 3: https://leetcode.com/problems/palindromic-substrings/discuss/105687/Python-Straightforward-with-Explanation-(Bonus-O(N)-solution)
        S = '#'.join(f'^{s}$')
        P = [0] * len(S)
        center = right = 0
        for i in range(1, len(S) - 1):
            if i < right:
                P[i] = min(right - i, P[2 * center - i])  # equals to i' = center - (i - center), where i' is the mirror of i centered at center
            # Attempt to expand palindrome centered at i
            while S[i + P[i] + 1] == S[i - P[i] - 1]:
                P[i] += 1
            # If palindrome centered at i expand past right, adjust center based on expanded palindrome
            if i + P[i] > right:
                center, right = i, i + P[i]
        return sum((p + 1) // 2 for p in P)

# Reference: https://leetcode.com/problems/longest-palindromic-substring/discuss/151144/Bottom-up-DP-Two-pointers
#======== <Solution 4> ========#
        # Form a bottom-up dp 2d array
        # dp[i][j] will be 1 if the string from index i to j is a palindrome
        dp = [[0] * len(s) for _ in range(len(s))]
        ans = 0
        
        # Every string with one character is a palindrome
        for i in range(len(s)):
            dp[i][i] = 1
            ans += dp[i][i]
        
        for cur_end in range(1, len(s)):
            for cur_start in range(cur_end - 1, -1, -1):
                #print(f'cur_start: {cur_start}, cur_end: {cur_end}')
                if s[cur_start] == s[cur_end]:
                    if cur_end - cur_start == 1 or dp[cur_start + 1][cur_end - 1]:
                        dp[cur_start][cur_end] = 1
                        ans += dp[cur_start][cur_end]
        return ans

#======== <Solution 5> ========#
        # Reference: https://leetcode.com/problems/palindromic-substrings/discuss/105707/Java-Python-DP-solution-based-on-longest-palindromic-substring
        dp = [[0] * len(s) for _ in range(len(s))]
        ans = 0
        for end in range(len(s)):
            for start in range(end, -1, -1):
                dp[start][end] = s[start] == s[end] and (end - start < 2 or dp[start + 1][end - 1])
                ans += dp[start][end]
        return ans

#======== <Solution 6> ========#
        ans = 0
        for i in range(len(s)):
            right = i
            while right < len(s) and s[i] == s[right]:
                ans += 1
                right += 1
            # s[i, right - 1] inclusive are equal characters e.g. "aaa"
            
            # while s[left] == s[right], s[left, right] inclusive is palindrome e.g. "baaab"
            left = i - 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
