class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Reference 1: https://leetcode.com/problems/subarray-sum-equals-k/solutions/341399/python-clear-explanation-with-code-and-example/
        # Reference 2: https://leetcode.com/problems/subarray-sum-equals-k/solutions/102111/python-simple-with-explanation/
        # Reference 3: https://leetcode.com/problems/subarray-sum-equals-k/solutions/190674/python-o-n-based-on-running-sum-concept-of-cracking-the-coding-interview-book/
        ans, presum, counter = 0, 0, {0: 1}
        for num in nums:
            presum += num
            ans += counter.get(presum - k, 0)  # Whenever presum has increased by k, we've found a subarray whose sum equals to k
            counter[presum] = counter.get(presum, 0) + 1  # Record the number of presum we've encountered so far
        return ans
