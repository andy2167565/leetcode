class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
#======== <Solution 1> ========#
        left = 0
        right = len(numbers) - 1
        
        while True:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1, right+1]

#======== <Solution 2> ========#
        seen = {}
        for i, num in enumerate(numbers):
            if target - num in seen:
                return [seen[target - num]+1, i+1]
            else:
                seen[num] = i
