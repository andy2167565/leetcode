class Solution:
    def minSwaps(self, s: str) -> int:
        open_braket = swap = 0
        for c in s:
            open_braket += 1 if c == '[' else -1
            if open_braket == -1:  # An unbalanced braket is found i.e. orphan ']'
                swap += 1
                open_braket = 1
        return swap
