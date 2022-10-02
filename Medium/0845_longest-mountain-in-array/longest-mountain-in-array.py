class Solution:
    def longestMountain(self, arr: List[int]) -> int:
#======== <Solution 1> ========#
        ans = 0
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l = r = i
                while l and arr[l] > arr[l - 1]:
                    l -= 1
                while r + 1 < len(arr) and arr[r] > arr[r + 1]:
                    r += 1
                ans = max(ans, r - l + 1)
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/longest-mountain-in-array/discuss/937652/Python-one-pass-O(1)-space-explained
        max_len, length, state = 0, 1, 'flat'
        for i in range(len(arr) - 1):
            if state in ['flat', 'up'] and arr[i + 1] > arr[i]:
                state, length = 'up', length + 1
            elif state == 'down' and arr[i + 1] > arr[i]:
                state, length = 'up', 2
            elif state in ['up', 'down'] and arr[i + 1] < arr[i]:
                state, length = 'down', length + 1
                max_len = max(length, max_len)
            else:
                state, length = 'flat', 1
        return max_len

# Reference: https://leetcode.com/problems/longest-mountain-in-array/discuss/135593/C%2B%2BJavaPython-1-pass-and-O(1)-space
#======== <Solution 3> ========#
        up, down = [0] * len(arr), [0] * len(arr)
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]: up[i] = up[i - 1] + 1
        for i in range(len(arr) - 1)[::-1]:
            if arr[i] > arr[i + 1]: down[i] = down[i + 1] + 1
        return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])

#======== <Solution 4> ========#
        up = down = ans = 0
        for i in range(1, len(arr)):
            if (down and arr[i - 1] < arr[i]) or arr[i - 1] == arr[i]:
                up = down = 0
            up += arr[i - 1] < arr[i]
            down += arr[i - 1] > arr[i]
            if up and down:
                ans = max(ans, up + down + 1)
        return ans
