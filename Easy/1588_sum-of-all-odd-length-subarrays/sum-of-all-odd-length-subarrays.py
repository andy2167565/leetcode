class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
#======== <Solution 1> ========#
        ans = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                if len(arr[i:j]) % 2:
                    ans += sum(arr[i:j])
        return ans

#======== <Solution 2> ========#
        ans = 0
        for i in range(len(arr)):
            cur_sum = 0
            for j in range(i, len(arr)):
                cur_sum += arr[j]
                if (j - i + 1) % 2:
                    ans += cur_sum
        return ans

#======== <Solution 3> ========#
        ans = 0
        for l in range(1, len(arr) + 1, 2):
            for i in range(len(arr) - l + 1):
                ans += sum(arr[i:i + l])
        return ans

#======== <Solution 4> ========#
        # Reference: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/854184/JavaC%2B%2BPython-O(N)-Time-O(1)-Space
        ans = 0
        for i, num in enumerate(arr):
            ans += ((i + 1) * (len(arr) - i) + 1) // 2 * num
        return ans
