class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        import collections
        ans, word_dict = 0, collections.defaultdict(list)
        for word in words:  # Sort words by their leading characters
            word_dict[word[0]].append(word)
        for ch in s:
            if ch in word_dict:
                for word in word_dict.pop(ch):
                    if len(word) == 1:  # Finished subsequence
                        ans += 1
                    else:  # Choose next character of word as the leading character
                        word_dict[word[1]].append(word[1:])
        return ans
