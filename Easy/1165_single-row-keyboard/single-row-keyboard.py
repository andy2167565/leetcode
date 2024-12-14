class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap = {c: i for i, c in enumerate(keyboard)}
        ans = curr = 0
        for c in word:
            ans += abs(hashmap[c] - curr)
            curr = hashmap[c]
        return ans
