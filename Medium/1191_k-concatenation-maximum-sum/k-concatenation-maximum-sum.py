class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/k-concatenation-maximum-sum/solutions/382808/python3-6-liner-kadane/
        def Kadane(arr, ans=0, curr=0):
            for num in arr:
                curr = max(num, num + curr)
                ans = max(ans, curr)
            return ans
        return ((k - 2) * max(sum(arr), 0) + Kadane(arr * 2)) % (10**9 + 7) if k > 1 else Kadane(arr) % (10**9 + 7)
