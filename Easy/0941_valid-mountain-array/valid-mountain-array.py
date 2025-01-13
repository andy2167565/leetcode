class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l, r, n = 0, len(arr) - 1, len(arr)
        if n < 3:
            return False
        while l + 1 < n - 1 and arr[l] < arr[l + 1]:
            l += 1
        while r - 1 and arr[r] < arr[r - 1]:
            r -= 1
        return l == r
