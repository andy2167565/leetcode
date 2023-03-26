class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # (1) k < numOnes
        # (2) numOnes <= k <= numOnes + numZeros
        # (3) k > numOnes + numZeros
        return min(k, numOnes, numOnes * 2 + numZeros - k)
