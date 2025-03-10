class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        return any(s == ''.join(words[:i]) for i in range(1, len(words) + 1))
