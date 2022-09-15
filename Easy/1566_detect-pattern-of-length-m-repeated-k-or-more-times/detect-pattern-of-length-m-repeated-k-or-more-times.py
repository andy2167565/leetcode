class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
#======== <Solution 1> ========#
        for i in range(m):
            count, consecutive = k, False
            for j in range(i, len(arr) - 2 * m + 1, m):
                if arr[j: j + m] == arr[j + m: j + 2 * m]:
                    count -= 1 + (not consecutive)
                    consecutive = True
                else:
                    if consecutive:
                        count, consecutive = k, False
                if not count: return True
        return False

#======== <Solution 2> ========#
        for i in range(len(arr) - m * k + 1):
            if arr[i: i + m] * k == arr[i: i + m * k]:
                return True
        return False

#======== <Solution 3> ========#
        return any(arr[i: i + m] * k == arr[i: i + m * k] for i in range(len(arr) - m * k + 1))

#======== <Solution 4> ========#
        streak = 0
        for i in range(len(arr) - m):
            streak = 0 if arr[i] != arr[i + m] else streak + 1
            if streak == m * (k - 1): return True
        return False
