class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max_idx = second_num = -1
        for i, num in enumerate(nums):
            if num > max_num:
                second_num, max_num, max_idx = max_num, num, i
            elif num > second_num:
                second_num = num
        return max_idx if max_num >= second_num * 2 else -1
