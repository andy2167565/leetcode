class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Reference: https://leetcode.com/problems/palindrome-pairs/solutions/79209/accepted-python-solution-with-explanation/
        ans, words = [], {word: i for i, word in enumerate(words)}
        for word, i in words.items():
            if word:  # Skip empty string
                for j in range(len(word) + 1):
                    prefix, suffix = word[:j], word[j:]
                    if prefix == prefix[::-1] and suffix[::-1] != word and suffix[::-1] in words:  # If suffix[::-1] == word then the word itself is a palindrome. Skip it so we don't count the pair of duplicate words [i, i].
                        ans.append([words[suffix[::-1]],  i])
                    if j < len(word) and suffix == suffix[::-1] and prefix[::-1] in words:  # Skip empty suffix, i.e. j == len(word), to avoid duplicates that are already added in prefix section
                        ans.append([i, words[prefix[::-1]]])
        return ans
