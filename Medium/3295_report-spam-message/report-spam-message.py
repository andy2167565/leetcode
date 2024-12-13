class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedWordsSet = set(bannedWords)
        return sum(word in bannedWordsSet for word in message) > 1
