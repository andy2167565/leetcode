class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        import collections
        def neighbors(code):
            for i, num in enumerate(code):
                for diff in (-1, 1):
                    yield code[:i] + str((int(num) + diff + 10) % 10) + code[i + 1:]

        deadSet = set(deadends)
        if '0000' not in deadSet:
            q, steps = collections.deque(['0000']), 0
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr == target:
                        return steps
                    for adj in neighbors(curr):
                        if adj not in deadSet:
                            deadSet.add(adj)  # Marked as visited
                            q.append(adj)
                steps += 1
        return -1
