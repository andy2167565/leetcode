class Solution:
    def greatestLetter(self, s: str) -> str:
        import collections, string
        counter = collections.Counter(s)
        return next((u for u in reversed(string.ascii_uppercase) if counter[u] and counter[u.lower()]), '')
