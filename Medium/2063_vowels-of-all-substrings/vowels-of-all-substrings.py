class Solution:
    def countVowels(self, word: str) -> int:
        # Reference: https://leetcode.com/problems/vowels-of-all-substrings/solutions/1563780/java-c-python-easy-and-concise-o-n/
        return sum((i + 1) * (len(word) - i) for i, c in enumerate(word) if c in 'aeiou')
