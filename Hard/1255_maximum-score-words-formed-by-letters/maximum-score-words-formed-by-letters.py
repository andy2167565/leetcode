class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Reference: https://leetcode.com/problems/maximum-score-words-formed-by-letters/solutions/425411/python-dfs-pruning/
        import collections
        self.max_score = 0
        words_score = [sum(score[ord(c) - ord('a')] for c in w) for w in words]
        words_counter = list(map(collections.Counter, words))  # Count the letters of each word
        def dfs(i, curr_score, counter):
            if curr_score + sum(words_score[i:]) <= self.max_score:  # It is not possible to get a higher score
                return
            self.max_score = max(self.max_score, curr_score)
            for j, letter_counter in enumerate(words_counter[i:], i):
                if not letter_counter - counter:  # Current word can be formed from current letters
                    dfs(j + 1, curr_score + words_score[j], counter - letter_counter)
        dfs(0, 0, collections.Counter(letters))
        return self.max_score
