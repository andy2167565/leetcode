class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
#======== <Solution 1> ========#
        import math
        count = 0
        for start in range(len(nums)):
            if not nums[start] % k:  # No need to start adding numbers if the divisors of the first number do not contain k
                for end in range(start, len(nums)):
                    if math.gcd(*nums[start: end + 1]) == k:
                        count += 1
        return count

#======== <Solution 2> ========#
        import math
        dp = [[-1] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        for start in range(len(nums) - 1):
            for end in range(start + 1, len(nums)):
                dp[start][end] = math.gcd(dp[start][end - 1], nums[end])
        return sum(dp[i][j] == k for i in range(len(nums)) for j in range(len(nums)))

#======== <Solution 3> ========#
        import math
        count = 0
        for start in range(len(nums)):
            cur_gcd = 0  # gcd of 0 and any number is equal to the number itself
            for end in range(start, len(nums)):
                cur_gcd = math.gcd(cur_gcd, nums[end])
                if cur_gcd == k:
                    count += 1
                elif cur_gcd < k:  # gcd cannot get larger if we keep adding numbers
                    break
        return count
