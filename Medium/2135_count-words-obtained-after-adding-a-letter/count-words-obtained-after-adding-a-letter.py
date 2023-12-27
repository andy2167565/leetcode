class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        import collections
        ans, counter, hashmap = 0, collections.Counter(targetWords), collections.defaultdict(int)  # Store the number of words that consist of the same letters
        for word in set(targetWords):
            hashmap[''.join(sorted(word))] += counter[word]
        for word in set(startWords):
            for i in range(26):
                new_word = ''.join(sorted(word + chr(97 + i)))
                if hashmap[new_word]:
                    ans += hashmap.pop(new_word)
        return ans
