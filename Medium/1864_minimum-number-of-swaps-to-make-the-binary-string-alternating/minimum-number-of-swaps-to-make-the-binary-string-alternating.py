class Solution:
    def minSwaps(self, s: str) -> int:
        def countSwaps(num):  # Count the number of chars at even positions which are not equal to num
            return sum(s[i] != num for i in range(0, len(s), 2))

        ones = s.count('1')
        zeros = len(s) - ones
        if abs(ones - zeros) > 1:  # Invalid
            return -1
        if zeros > ones:  # Zero starts first
            return countSwaps('0')
        if zeros < ones:  # One starts first
            return countSwaps('1')
        return min(countSwaps('0'), countSwaps('1'))  # Get min swaps between 2 cases
