class Solution:
    def longestPalindrome(self, s: str) -> int:
#======== <Solution 1> ========#
        odd_letters = set()
        for c in s:
            if c not in odd_letters:
                odd_letters.add(c)
            else:
               odd_letters.remove(c)
        return len(s) - len(odd_letters) + 1 if len(odd_letters) else len(s)

#======== <Solution 2> ========#
        import collections
        odd_counts = sum(v & 1 for v in collections.Counter(s).values())  # v & 1 == 1 if v is odd, 0 if v is even
        return len(s) - odd_counts + bool(odd_counts)
