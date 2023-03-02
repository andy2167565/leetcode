class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Reference 1: https://leetcode.com/problems/alien-dictionary/solutions/70137/16-18-lines-python-30-lines-c/comments/544533
        # Reference 2: https://leetcode.com/problems/alien-dictionary/solutions/156130/python-solution-with-detailed-explanation-91/
        import collections
        chars = set(''.join(words))  # Get all unique chars
        graph = {c: [] for c in chars}  # Store chars after c in alien lexicographical order
        degrees = {c: 0 for c in chars}  # The char with larger degree is after the one with smaller degree
        for w1, w2 in zip(words, words[1:]):  # Compare with next adjacent word
            for c1, c2 in zip(w1, w2):
                if c1 != c2:  # c2 is after c1
                    graph[c1].append(c2)
                    degrees[c2] += 1
                    break  # Each pair of words only presents information about one pair of letters
            else:  # The first min(len(w1), len(w2)) chars do not differ
                if len(w1) > len(w2):  # The shorter string should be the lexicographically smaller one
                    return ''
        queue = collections.deque(filter(lambda c: not degrees[c], degrees.keys()))  # Chars with degree 0
        ans = ''
        while queue:
            c = queue.popleft()
            ans += c
            for next_char in graph[c]:
                degrees[next_char] -= 1
                if not degrees[next_char]:  # All chars before next_char have been appended to ans
                    queue.append(next_char)
        return ans * (set(ans) == chars)  # Check if all chars have been added to ans i.e. all degrees hit 0
