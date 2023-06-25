class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        return sum(words[i][0] == words[j][1] and words[i][1] == words[j][0] for i in range(len(words) - 1) for j in range(i + 1, len(words)))
