class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        import itertools, collections
        ans = {0, firstPerson}
        for _, group in itertools.groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):  # Sort and group meetings by time
            queue, graph = set(), collections.defaultdict(list)
            for x, y, _ in group:  # Collect people who know the secret
                graph[x].append(y)
                graph[y].append(x)
                if x in ans:
                    queue.add(x)
                if y in ans:
                    queue.add(y)
            queue = collections.deque(queue)
            while queue:  # Share the secret with the people they meet
                for p in graph[queue.popleft()]:
                    if p not in ans:
                        ans.add(p)
                        queue.append(p)
        return ans
