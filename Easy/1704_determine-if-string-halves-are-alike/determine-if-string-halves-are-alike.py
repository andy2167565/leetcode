class Solution:
    def halvesAreAlike(self, s: str) -> bool:
# My Post: https://leetcode.com/problems/determine-if-string-halves-are-alike/discuss/2591599/Python-5-Solutions-or-Easy-or-Clean-or-Straightforward
#======== <Solution 1> ========#
        vowels, count = 'aeiouAEIOU', 0
        for i in range(len(s) // 2):
            count += (s[i] in vowels) - (s[~i] in vowels)
        return not count

#======== <Solution 2> ========#
        s, count = [s[:len(s) // 2], s[len(s) // 2:]], 0
        for i, half in enumerate(s):
            for vowel in set(half).intersection('aeiouAEIOU'):
                count += half.count(vowel) if not i else -half.count(vowel)
        return not count

#======== <Solution 3> ========#
        from collections import Counter
        C, count = list(map(Counter, (s[:len(s) // 2], s[len(s) // 2:]))), 0
        for i, half in enumerate(C):
            for char in half:
                if char in 'aeiouAEIOU':
                    count += half[char] if not i else -half[char]
        return not count

#======== <Solution 4> ========#
        return sum(char in 'aeiouAEIOU' for char in s[:len(s) // 2]) == sum(char in 'aeiouAEIOU' for char in s[len(s) // 2:])

#======== <Solution 5> ========#
        count = 0
        for i, char in enumerate(s):
            if char in 'aeiouAEIOU':
                count += 1 if i < len(s) // 2 else -1
        return not count
