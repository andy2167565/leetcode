class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
#======== <Solution 1> ========#
        import collections
        freqs = collections.defaultdict(int)
        for word in words:  # Store the frequency of every prefixes for each word
            for i in range(len(word)):
                freqs[word[:i + 1]] += 1
        return [sum(freqs[word[:i + 1]] for i in range(len(word))) for word in words]

#======== <Solution 2> ========#
        trie = {}
        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
                curr['score'] = curr.get('score', 0) + 1  # Store the occurrence of the prefix at each letter
        ans = []
        for word in words:
            curr, score = trie, 0
            for c in word:
                curr = curr[c]
                score += curr['score']
            ans.append(score)
        return ans
