class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        l = curr_sum = 0
        ans, prev_min = float('inf'), [float('inf')] * len(arr)  # prev_min[i]: The minimum length of qualified subarray in arr[:i + 1]
        for r, num in enumerate(arr):
            curr_sum += num
            while curr_sum > target:  # Move the sliding window forward
                curr_sum -= arr[l]
                l += 1
            if curr_sum == target:
                curr_len = r - l + 1
                ans = min(ans, curr_len + prev_min[l - 1])
                prev_min[r] = min(curr_len, prev_min[r - 1])
            else:
                prev_min[r] = prev_min[r - 1]
        return ans if ans < float('inf') else -1
