class Solution:
    def shortestPalindrome(self, s: str) -> str:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/shortest-palindrome/discuss/60099/AC-in-288-ms-simple-brute-force
        reverse = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(reverse[i:]):
                return reverse[:i] + s

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/shortest-palindrome/discuss/60250/My-recursive-Python-solution
        if not s or len(s) == 1: return s
        index = 0
        for i in reversed(range(len(s))):
            if s[i] == s[index]:
                index += 1
        return s[index:][::-1] + self.shortestPalindrome(s[:index - len(s)]) + s[index - len(s):]

# Reference (Explanation): https://leetcode.com/problems/shortest-palindrome/discuss/60113/Clean-KMP-solution-with-super-detailed-explanation
#======== <Solution 3> ========#
        palindrome = s + '#' + s[::-1]
        failure = [0] * len(palindrome)
        index = 0
        for i, c in enumerate(palindrome[1:], 1):
            while index > 0 and palindrome[index] != c:
                index = failure[index - 1]
            index += palindrome[index] == c
            failure[i] = index
        return palindrome[len(s) + 1: -failure[-1]] + s
        #return s[::-1][:-failure[-1]] + s

#======== <Solution 4> ========#
        palindrome = s + '#' + s[::-1]
        count = [0]
        for i in range(1, len(palindrome)):
            index = count[i - 1]
            while index > 0 and palindrome[index] != palindrome[i]:
                index = count[index - 1]
            count.append(index + (palindrome[index] == palindrome[i]))
        return s[count[-1]:][::-1] + s
