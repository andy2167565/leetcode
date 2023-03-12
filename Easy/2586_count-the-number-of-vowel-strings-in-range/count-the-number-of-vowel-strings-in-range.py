class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
#======== <Solution 1> ========#
        return sum(word[0] in 'aeiou' and word[-1] in 'aeiou' for word in words[left: right + 1])

#======== <Solution 2> ========#
        return sum({word[0], word[-1]}.issubset(set('aeiou')) for word in words[left: right + 1])
