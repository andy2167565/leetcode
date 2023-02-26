class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left, right, ans = 0, sum(nums), []
        for num in nums:
            right -= num
            ans.append(abs(left - right))
            left += num
        return ans
