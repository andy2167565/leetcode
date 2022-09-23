class Solution:
    def longestPalindrome(self, s: str) -> str:
#======== <Solution 1> ========#
        max_start = max_end = center_left = center_right = 0
        while center_right < len(s):
            cur_left, cur_right = center_left, center_right
            while cur_left >= 0 and cur_right < len(s) and s[cur_left] == s[cur_right]:
                if cur_right - cur_left > max_end - max_start:  # palindrome longer than existing one
                    max_start, max_end = cur_left, cur_right
                cur_left -= 1
                cur_right += 1
            if center_left == center_right:
                center_right += 1  # even case, like "abba"
            else:
                center_left += 1  # odd case, like "aba"
        return s[max_start: max_end + 1]

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/longest-palindromic-substring/discuss/2925/Python-O(n2)-method-with-some-optimization-88ms.
        max_start, max_len = 0, 1
        for i in range(1, len(s)):
            cur_start = i - max_len - 1
            if cur_start >= 0 and s[cur_start: i + 1] == s[cur_start: i + 1][::-1]:
                max_start = cur_start
                max_len += 2
                continue
            
            cur_start += 1
            if cur_start >= 0 and s[cur_start: i + 1] == s[cur_start: i + 1][::-1]:
                max_start = cur_start
                max_len += 1
        return s[max_start: max_start + max_len]

#======== <Solution 3> ========#
        # Reference 1: https://leetcode.com/problems/longest-palindromic-substring/discuss/3337/Manacher-algorithm-in-Python-O(n)
        # Reference 2: https://www.youtube.com/watch?v=YVZttWzvyw8&ab_channel=FluentAlgorithms
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
        max_radius, max_center = max((v, i) for i, v in enumerate(P))
        # e.g.                          babad             ^#b#a#b#a#d#$ 
        # Index of s elements      [0, 1, 2, 3, 4]       [2, 4, 6, 8, 10]
        # Palindrome                     aba                 #a#b#a#
        # Center of palindrome            2                     6
        # Radius of palindrome            1                     3
        # Range of palindrome    1(2 - 1) ~ 3(2 + 1)   3(6 - 3) ~ 9(6 + 3)
        # Therefore the palindrome is s[1: 4] = s[3 // 2: 9 // 2] = s[(6 - 3) // 2: (6 + 3) // 2]
        return s[(max_center - max_radius) // 2: (max_center + max_radius) // 2]

# Reference: https://leetcode.com/problems/longest-palindromic-substring/discuss/151144/Bottom-up-DP-Two-pointers
#======== <Solution 4> ========#
        # Form a bottom-up dp 2d array
        # dp[i][j] will be True if the string from index i to j is a palindrome
        dp = [[False] * len(s) for _ in range(len(s))]
        
        # Every string with one character is a palindrome
        for i in range(len(s)):
            dp[i][i] = True
        
        max_start, max_len = 0, 1
        for cur_end in range(1, len(s)):
            for cur_start in range(cur_end - 1, -1, -1):
                #print(f'cur_start: {cur_start}, cur_end: {cur_end}')
                if s[cur_start] == s[cur_end]:
                    if cur_end - cur_start == 1 or dp[cur_start + 1][cur_end - 1]:
                        dp[cur_start][cur_end] = True
                        cur_len = cur_end - cur_start + 1
                        if max_len < cur_len:
                            max_start = cur_start
                            max_len = cur_len
        return s[max_start: max_start + max_len]

#======== <Solution 5> ========#
        max_start, max_len = 0, 1
        for i in range(len(s)):
            right = i
            while right < len(s) and s[i] == s[right]:
                right += 1
            # s[i, right - 1] inclusive are equal characters e.g. "aaa"
            
            # while s[left] == s[right], s[left, right] inclusive is palindrome e.g. "baaab"
            left = i - 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            # s[left + 1, right - 1] inclusive is palindromic
            cur_len = right - left - 1
            if cur_len > max_len:
                max_len = cur_len
                max_start = left + 1
            
        return s[max_start: max_start + max_len]
