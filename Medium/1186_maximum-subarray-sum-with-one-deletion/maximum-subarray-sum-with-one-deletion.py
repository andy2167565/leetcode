class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ans = zero = one = float('-inf')
        for num in arr:
            one = max(zero, num + one)  # One deletion
            zero = max(num, num + zero)  # No deletion
            ans = max(ans, one, zero)
        return ans
