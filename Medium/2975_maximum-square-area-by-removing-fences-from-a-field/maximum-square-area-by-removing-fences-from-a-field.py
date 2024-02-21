class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def allDiffs(l, fences):
            fences.extend((1, l))
            return {abs(fences[i] - fences[j]) for i in range(len(fences)) for j in range(i + 1, len(fences))}
        ans = max(allDiffs(m, hFences) & allDiffs(n, vFences), default=-1)
        return ans**2 % (10**9 + 7) if ans != -1 else -1
