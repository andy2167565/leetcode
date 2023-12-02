class Solution:
    def minJumps(self, arr: List[int]) -> int:
        import collections
        hashmap = collections.defaultdict(list)
        for i, num in enumerate(arr):
            hashmap[num].append(i)
        queue, visited = collections.deque([(0, 0)]), set()
        while queue:
            index, steps = queue.popleft()
            if index == len(arr) - 1:
                return steps
            for nxt in [index - 1, index + 1] + hashmap[arr[index]]:
                if index != nxt and 0 <= nxt < len(arr) and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
            hashmap.pop(arr[index])
