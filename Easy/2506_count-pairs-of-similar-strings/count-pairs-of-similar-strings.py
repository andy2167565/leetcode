class Solution:
    def similarPairs(self, words: List[str]) -> int:
#======== <Solution 1> ========#
        ans = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if set(words[i]) == set(words[j]):
                    ans += 1
        return ans

#======== <Solution 2> ========#
        import collections
        ans, freq = 0, collections.defaultdict(int)
        for word in words:
            mask = 0
            for c in word:
                mask |= (1 << (ord(c) - ord('a')))
                # e.g.             zyxwvutsrqponmlkjihgfedcba
                # mask of 'aabc' =                        111
                # mask of 'abcd' =                       1111
                # mask of 'nba'  =             10000000000011
            ans += freq[mask]
            freq[mask] += 1
        return ans
