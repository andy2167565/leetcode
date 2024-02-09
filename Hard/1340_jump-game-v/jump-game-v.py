class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        import collections, functools
        n, graph = len(arr), collections.defaultdict(list)

        def jump(iterator, stack=[]):
            for curr in iterator:
                while stack and arr[stack[-1]] < arr[curr] and abs(stack[-1] - curr) <= d:
                    graph[stack.pop()].append(curr)
                stack.append(curr)
        
        jump(range(n))  # Jump from right to left
        jump(reversed(range(n)))  # Jump from left to right
        
        @functools.cache
        def backtrace(i):
            return 1 + max(map(backtrace, graph[i]), default=0)
        
        return max(map(backtrace, range(n)))  # Iterate end indexes to find the best route
