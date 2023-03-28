class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Reference: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/solutions/754721/c-python-7-line-intuitive-constant-space-dp/
        ans = odd = even = 0
        for num in arr:
            even += 1
            if num % 2:
                odd, even = even, odd
            ans = (ans + odd) % (10**9 + 7)
        return ans
