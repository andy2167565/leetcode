class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return sum(not set(word) & set(brokenLetters) for word in text.split(' '))
