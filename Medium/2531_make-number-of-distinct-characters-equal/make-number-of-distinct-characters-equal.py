class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        import collections
        freq1, freq2 = collections.Counter(word1), collections.Counter(word2)
        n1, n2 = len(freq1), len(freq2)
        for c1 in freq1:
            for c2 in freq2:
                if c1 == c2:  # No need to swap
                    if n1 == n2:
                        return True
                else:  # Swap c1 with c2
                    if n1 + (not freq1[c2]) - (freq1[c1] == 1) == n2 + (not freq2[c1]) - (freq2[c2] == 1):
                        return True
        return False
