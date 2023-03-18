class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        import itertools
        def compress(word):  # e.g. 'heeellooo': [(h, 1), (e, 3), (l, 2), (o, 3)]
            return [(c, len(list(g))) for c, g in itertools.groupby(word)]

        def isStretchy(word):
            word_group = compress(word)
            if len(s_group) != len(word_group):  # Mismatch number of groups
                return False
            for i in range(len(s_group)):
                if s_group[i][0] != word_group[i][0]:  # Mismatch letter
                    return False
                if s_group[i][1] != word_group[i][1] and s_group[i][1] < max(3, word_group[i][1]):  # Length of char in s is smaller than either 3 or length of char in word
                    return False
            return True

        s_group = compress(s)
        return sum(isStretchy(word) for word in words)
