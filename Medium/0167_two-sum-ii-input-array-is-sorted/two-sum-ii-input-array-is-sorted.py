class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
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
