class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
#======== <Solution 1> ========#
        return len(set(b - a for a, b in zip(sorted(arr), sorted(arr)[1:]))) == 1

#======== <Solution 2> ========#
        return arr.sort() or all(j - i == arr[1] - arr[0] for i, j in zip(arr, arr[1:]))

#======== <Solution 3> ========#
        # Reference 1: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/discuss/720152/O(n)-time-O(1)-space
        # Reference 2: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/discuss/720200/Clean-Python-3-O(N)
        m = min(arr)
        gap = (max(arr) - m) / (len(arr) - 1)
        if not gap: return True
        i = 0
        while i < len(arr):
            if arr[i] == m + i * gap:
                i += 1
            else:
                pos, r = int((arr[i] - m) / gap), (arr[i] - m) % gap
                if r or arr[pos] == arr[i]: return False
                arr[pos], arr[i] = arr[i], arr[pos]
        return True

#======== <Solution 4> ========#
        m, M, n, s = min(arr), max(arr), len(arr), set(arr)
        diff, r = divmod(M - m, n - 1)
        if r: return False
        for _ in range(n):
            if m not in s: return False
            m += diff
        return True

#======== <Solution 5> ========#
        import heapq
        a, b = heapq.nsmallest(2, arr)
        gap = b - a
        acc = range(a, a + gap * len(arr), gap) if gap else [arr[0]]
        return set(acc) == set(arr)
