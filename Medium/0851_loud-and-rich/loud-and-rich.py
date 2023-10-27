class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        import collections
        hashmap, answer = collections.defaultdict(list), [-1] * len(quiet)
        for a, b in richer:
            hashmap[b].append(a)
        def dfs(node):
            if answer[node] < 0:
                answer[node] = min([dfs(adj) for adj in hashmap[node]] + [node], key=lambda x: quiet[x])
            return answer[node]
        return list(map(dfs, range(len(quiet))))
