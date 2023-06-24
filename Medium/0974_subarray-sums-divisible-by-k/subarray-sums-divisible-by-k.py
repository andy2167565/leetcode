class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/subarray-sums-divisible-by-k/solutions/310767/python-concise-explanation-and-proof/
        ans = prefix = 0
        mod_count = [1] + [0] * k
        for num in nums:
            prefix = (prefix + num) % k
            ans += mod_count[prefix]
            mod_count[prefix] += 1
        return ans
