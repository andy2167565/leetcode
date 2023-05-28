class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        import math
        positives, negatives = [], []
        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
        if not (positives or negatives):  # Only consists of 0s
            return 0
        if len(negatives) % 2:  # There are odd number of negatives
            if len(negatives) > 1:  # Make the number of remaining negatives even
                negatives.remove(max(negatives))
            elif positives:  # There are some positives and 1 negative
                return math.prod(positives)
            # (1) Some 0s and 1 negative
            # (2) Only 1 negative
            else:
                return max(nums)
        return math.prod(positives) * math.prod(negatives)
