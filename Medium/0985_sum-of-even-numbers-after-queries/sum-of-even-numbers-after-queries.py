class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans, even_sum = [], sum(num for num in nums if not num % 2)
        for v, i in queries:
            if not nums[i] % 2:  # An even value may change to either an even or odd value
                even_sum -= nums[i]
            nums[i] += v
            if not nums[i] % 2:  # An even or odd value changed to an even value
                even_sum += nums[i]
            ans.append(even_sum)
        return ans
