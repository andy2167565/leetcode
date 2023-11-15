class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        import collections
        words, lowercase, vowel = collections.defaultdict(), collections.defaultdict(), collections.defaultdict()
        for w in wordlist[::-1]:  # Reverse wordlist to get the first match of each hashmap
            words[w] = w
            lowercase[w.lower()] = w
            vowel[re.sub('[aeiou]', '*', w.lower())] = w  # Mask the vowels in the word
        return [words.get(w) or lowercase.get(w.lower()) or vowel.get(re.sub('[aeiou]', '*', w.lower()), '') for w in queries]
