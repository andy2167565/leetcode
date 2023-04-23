class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
#======== <Solution 1> ========#
        ans, counter = [0] * (len(nums) - k + 1), [0] * 50  # counter[i]: Number of i = 50 + num in nums where num is negative
        for i, num in enumerate(nums):
            if num < 0:  # Only count negative numbers
                counter[num + 50] += 1  # Add 50 so we can iterate counter in ascending order later
            if i >= k and nums[i - k] < 0:  # A negative number is removed from the sliding subarray
                counter[nums[i - k] + 50] -= 1
            if i >= k - 1:
                curr_count = 0
                for adjusted_num, count in enumerate(counter):  # Start counting in ascending order
                    curr_count += count
                    if curr_count >= x:  # There are enough negative numbers
                        ans[i - k + 1] = adjusted_num - 50
                        break
        return ans

#======== <Solution 2> ========#
        import sortedcontainers
        ans, subarray = [], sortedcontainers.SortedList()
        for i, num in enumerate(nums):
            subarray.add(num)
            if i >= k:
                subarray.remove(nums[i - k])
            if i >= k - 1:
                ans.append(min(0, subarray[x - 1]))
        return ans
