class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/117723/Python-standard-DP-solution-with-explanation
        ans, count, last = 0, 0, -1
        for i, num in enumerate(nums):
            if num <= right:
                if left <= num:
                    count = i - last
                ans += count
            else:
                count, last = 0, i
        return ans

# Reference: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/1278426/JS-Python-Java-C%2B%2B-or-Easy-Triangular-Number-Solution-w-Explanation
#======== <Solution 2> ========#
        ans = low = mid = 0
        for num in nums:
            if num > right:
                mid = 0
            else:
                mid += 1
                ans += mid
            if num >= left:
                low = 0
            else:
                low += 1
                ans -= low
        return ans

#======== <Solution 3> ========#
        ans = low = mid = 0
        for num in nums:
            mid = mid + 1 if num <= right else 0
            low = low + 1 if num < left else 0
            ans += mid - low
        return ans
