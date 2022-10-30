class Solution:
    def oddString(self, words: List[str]) -> str:
#======== <Solution 1> ========#
        import collections
        diff_list = []
        for word in words:
            tuple = ()
            for j in range(1, len(word)):
                tuple += (ord(word[j]) - ord(word[j - 1]), )
            diff_list.append(tuple)
        return words[diff_list.index(collections.Counter(diff_list).most_common()[-1][0])]

#======== <Solution 2> ========#
        diff_dict = defaultdict(list)
        for word in words:
            diff = [ord(b) - ord(a) for a, b in zip(word[:-1], word[1:])]
            diff_dict[tuple(diff)].append(word)
        for _, word_list in diff_dict.items():
            if len(word_list) == 1:
                return word_list[0]

#======== <Solution 3> ========#
        diff = lambda word: [ord(word[i]) - ord(word[i - 1]) for i in range(1, len(word))]
        words.sort(key=diff)
        return words[0] if diff(words[0]) != diff(words[1]) else words[-1]
