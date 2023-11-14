class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        import collections
        groups = [-1] * n
        graph = collections.defaultdict(list)
        for a, b in dislikes:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)

        def dfs(person, group):
            groups[person] = group
            for hater in graph[person]:
                if groups[hater] != -1 and groups[hater] != 1 - group:  # The person and his/her hater are in the same group
                    return False
                if groups[hater] == -1 and not dfs(hater, 1 - group):
                    return False
            return True

        return not any(groups[i] == -1 and not dfs(i, 0) for i in range(n))
