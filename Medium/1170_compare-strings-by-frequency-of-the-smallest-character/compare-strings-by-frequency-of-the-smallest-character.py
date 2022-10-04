class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
#======== <Solution 1> ========#
        Q = [query.count(min(query)) for query in queries]
        W = [word.count(min(word)) for word in words]
        ans = []
        for q in Q:
            ans.append(0)
            for w in W:
                if q < w:
                    ans[-1] += 1
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/discuss/366927/Python-2-liner
        import bisect
        f = lambda word: word.count(min(word))
        words = sorted(map(f, words))
        return [len(words) - bisect.bisect(words, f(query)) for query in queries]

#======== <Solution 3> ========#
        import itertools
        f = lambda word: word.count(min(word))
        counts = [0] * 11
        for count in map(f, words):
            counts[count] += 1
        buckets = [len(words) - acc for acc in itertools.accumulate(counts)]
        return [buckets[f(query)] for query in queries]
