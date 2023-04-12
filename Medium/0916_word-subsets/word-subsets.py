class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
#======== <Solution 1> ========#
        import collections
        counter = collections.Counter()
        for word in words2:
            counter |= collections.Counter(word)  # Take the maximum occurrence for each letter
        return [word for word in words1 if not counter - collections.Counter(word)]

#======== <Solution 2> ========#
        import collections, functools, operator
        counter = functools.reduce(operator.or_, (collections.Counter(word) for word in words2))
        return [word for word in words1 if counter & collections.Counter(word) == counter]
