class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(s in word for s in patterns)
