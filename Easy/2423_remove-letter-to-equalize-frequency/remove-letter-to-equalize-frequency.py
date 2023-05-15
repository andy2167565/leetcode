class Solution:
    def equalFrequency(self, word: str) -> bool:
#======== <Solution 1> ========#
        import collections
        return any(len(set(collections.Counter(word[:i] + word[i+1:]).values())) == 1 for i in range(len(word)))

#======== <Solution 2> ========#
        import collections
        counter = collections.Counter(word)
        for c in word:
            counter[c] -= 1
            if not counter[c]:
                counter.pop(c)
            if len(set(counter.values())) == 1:
                return True
            counter[c] += 1
        return False
