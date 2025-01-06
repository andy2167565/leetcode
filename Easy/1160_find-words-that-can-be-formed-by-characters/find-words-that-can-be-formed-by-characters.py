class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        import collections
        counter = collections.Counter(chars)
        return sum(len(word) for word in words if collections.Counter(word) <= counter)
