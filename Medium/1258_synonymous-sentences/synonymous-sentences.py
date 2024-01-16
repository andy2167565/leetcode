class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        import collections
        graph = collections.defaultdict(set)
        for s, t in synonyms:
            graph[s].add(t)
            graph[t].add(s)
        ans, stack = set(), [text]
        while stack:
            curr_text = stack.pop()
            ans.add(curr_text)
            curr_words = curr_text.split()
            for i, word in enumerate(curr_words):
                for synonym in graph[word]:
                    new_text = ' '.join(curr_words[:i] + [synonym] + curr_words[i + 1:])
                    if new_text not in ans:
                        stack.append(new_text)
        return sorted(ans)
