class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = ans = 0
        hashmap = {}
        for i in range(len(nums)):
            cur_sum += nums[i]
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
            if i >= k:  # Length of current subarray is larger than k, remove the first element of the subarray
                cur_sum -= nums[i - k]
                hashmap[nums[i - k]] -= 1
                if not hashmap.get(nums[i - k], 0):
                    hashmap.pop(nums[i - k])
            if len(hashmap) == k:  # All the elements of the subarray are distinct
                ans = max(ans, cur_sum)
        return ans
