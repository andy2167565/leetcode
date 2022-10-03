class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
# Reference: https://leetcode.com/problems/largest-time-for-given-digits/discuss/200693/JavaPython-3-11-liner-O(64)-w-comment-6-ms.
#======== <Solution 1> ========#
        ans = ''
        for i, a in enumerate(arr):
            for j, b in enumerate(arr):
                for k, c in enumerate(arr):
                    if i == j or i == k or j == k:
                        continue
                    hour, minute = str(a) + str(b), str(c) + str(arr[6 - i - j - k])
                    if hour < '24' and minute < '60':
                        ans = max(ans, f'{hour}:{minute}')
        return ans

#======== <Solution 2> ========#
        import itertools
        for time in itertools.permutations(sorted(arr, reverse=True)):
            if time[:2] < (2, 4) and time[2] < 6:
                return f'{time[0]}{time[1]}:{time[2]}{time[3]}'
        return ''
