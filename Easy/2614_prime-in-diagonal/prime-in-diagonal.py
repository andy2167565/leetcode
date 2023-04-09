class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if not num % i:
                    return False
            return True
        ans = 0
        for i in range(len(nums)):
            if isPrime(nums[i][i]):
                ans = max(ans, nums[i][i])
            if isPrime(nums[i][len(nums) - i - 1]):
                ans = max(ans, nums[i][len(nums) - i - 1])
        return ans
