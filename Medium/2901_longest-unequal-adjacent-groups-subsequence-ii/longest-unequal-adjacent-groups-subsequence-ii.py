class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        import functools

        @functools.cache
        def dfs(i):
            candidates = []
            for j in range(i + 1, len(groups)):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and sum(a != b for a, b in zip(words[i], words[j])) == 1:
                    candidates = max(candidates, dfs(j), key=len)
            return [words[i]] + candidates

        return max([dfs(i) for i in range(len(groups))], key=len)
