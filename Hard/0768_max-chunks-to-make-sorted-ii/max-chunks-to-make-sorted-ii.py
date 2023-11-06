class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
#======== <Solution 1> ========#
        import collections
        ans, original_counter, result_counter = 0, collections.Counter(), collections.Counter()
        for a, b in zip(arr, sorted(arr)):
            original_counter[a] += 1
            result_counter[b] += 1
            ans += original_counter == result_counter
        return ans

#======== <Solution 2> ========#
        ans = original_sum = sorted_sum = 0
        for a, b in zip(arr, sorted(arr)):
            original_sum += a
            sorted_sum += b
            ans += original_sum == sorted_sum
        return ans
