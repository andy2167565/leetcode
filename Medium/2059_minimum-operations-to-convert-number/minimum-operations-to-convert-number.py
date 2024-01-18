class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        import collections
        ans, seen, queue = 0, set(), collections.deque([start])
        while queue:
            for _ in range(len(queue)):
                val = queue.popleft()
                if val == goal:
                    return ans
                if 0 <= val <= 1000 and val not in seen:
                    seen.add(val)
                    for num in nums:
                        queue.extend([val + num, val - num, val ^ num])
            ans += 1
        return -1
