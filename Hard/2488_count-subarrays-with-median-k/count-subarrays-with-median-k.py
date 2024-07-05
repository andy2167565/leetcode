class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/count-subarrays-with-median-k/solutions/2851944/java-python-3-c-1-pass-o-n-codes-count-the-prefix-sum-of-the-balance-of-greater-samller/
        import collections
        prefix_balance = collections.Counter([0])  # The frequency of dummy value 0 is 1
        running_balance = ans = 0
        found = False
        for num in nums:
            if num < k:
                running_balance -= 1
            elif num > k:
                running_balance += 1
            else:
                found = True
            if found:
                ans += prefix_balance[running_balance] + prefix_balance[running_balance - 1]
            else:
                prefix_balance[running_balance] += 1
        return ans
