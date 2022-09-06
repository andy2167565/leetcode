class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        result = nums[0]
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            result = max(result, current_sum)
        return result

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer
        dp = [[0] * len(nums) for i in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], nums[i] + dp[1][i - 1])
            dp[0][i] = max(dp[0][i - 1], dp[1][i])
        return dp[0][-1]

#======== <Solution 3> ========#
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
        return max(nums)

#======== <Solution 4> ========#
        from itertools import accumulate
        return max(accumulate(nums, lambda acc, x: max(x, acc + x)))

#======== <Solution 5> ========#
        # Reference: https://leetcode.com/problems/maximum-subarray/discuss/199163/Python-O(N)-Divide-and-Conquer-solution-with-explanations
        def divide_and_conquer(l, r):
            # This function returns four values
            # 1) head_sum - maximum sum if we start adding from head
            # 2) tail_sum - maximum sum if we start adding from tail
            # 3) sum_ - total sum of this section
            # 4) max_sum - maximum sum we have seen so far anywhwere
            
            if l == r: # Base case
                return nums[l], nums[l], nums[l], nums[l]
            
            mid = (l + r) // 2
            
            # Find the values for left and right section
            head_sum_l, tail_sum_l, sum_l, max_sum_l = divide_and_conquer(l, mid)
            head_sum_r, tail_sum_r, sum_r, max_sum_r = divide_and_conquer(mid + 1, r)
            
            # head_sum is maximum of head_sum left or entire sum of left array + head_sum right
            head_sum = max(head_sum_l, sum_l + head_sum_r)
            
            # tail_sum is maximum of tail_sum right or tail_sum left + sum of entire right array
            tail_sum = max(tail_sum_r, tail_sum_l + sum_r)
            
            # sum_ is just sum of left and right
            sum_ = sum_l + sum_r
            
            # max_sum is either max_sum seen so far on left or right or the middle (tail of left and head of right)
            max_sum = max(max_sum_l, max_sum_r, tail_sum_l + head_sum_r)
            
            return head_sum, tail_sum, sum_, max_sum
        
        _, _, _, max_sum = divide_and_conquer(0, len(nums) - 1)
        return max_sum
