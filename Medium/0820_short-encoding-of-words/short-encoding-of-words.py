class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
#======== <Solution 1> ========#
        words.sort(key=len, reverse=True)
        s = ''
        for word in words:
            if word + '#' not in s:
                s += word + '#'
        return len(s)

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/short-encoding-of-words/solutions/125811/c-java-python-easy-understood-solution-with-explanation/
        s = set(words)
        for word in words:
            for i in range(1, len(word)):
                s.discard(word[i:])
        return sum(len(word) + 1 for word in s)

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/short-encoding-of-words/solutions/125784/trie-solution/comments/868292
        trie, ans = {}, 0  # e.g. trie = {'e': {'m': {'i': {'t': {'$': 5}}}}, 'l': {'l': {'e': {'b': {'$': 5}}}}}
        for word in words:
            node = trie
            for c in reversed(word):
                if '$' in node:  # Update the existing word to longer one, e.g. 'lame' -> 'flame'
                    ans -= node.pop('$')
                node = node.setdefault(c, {})
            if not node:  # A new word has been created in trie
                node['$'] = len(word) + 1
                ans += node['$']
        return ans
