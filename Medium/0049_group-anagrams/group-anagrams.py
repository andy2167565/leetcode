class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[tuple(sorted(word))].append(word)
        return list(anagrams.values())
