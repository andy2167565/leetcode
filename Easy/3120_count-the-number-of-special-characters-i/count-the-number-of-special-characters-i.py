class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        import string
        return sum(c in word and c.upper() in word for c in string.ascii_lowercase)
