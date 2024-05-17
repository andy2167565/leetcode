class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/maximum-score-of-a-good-subarray/solutions/1108333/java-c-python-two-pointers/
        ans = mini = nums[k]
        i = j = k
        n = len(nums)
        while i > 0 or j < n - 1:
            if (nums[i - 1] if i else 0) < (nums[j + 1] if j < n - 1 else 0):
                j += 1
            else:
                i -= 1
            mini = min(mini, nums[i], nums[j])
            ans = max(ans, mini * (j - i + 1))
        return ans
