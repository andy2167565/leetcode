class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
#======== <Solution 1> ========#
        import collections, heapq
        freqs = collections.Counter(words)
        return heapq.nsmallest(k, freqs, key=lambda word: (-freqs[word], word))

#======== <Solution 2> ========#
        freqs = {}
        for word in words:
            freqs[word] = freqs.get(word, 0) + 1
        return sorted(freqs, key=lambda word: (-freqs[word], word))[:k]
