# Reference: https://leetcode.com/problems/random-pick-with-weight/solutions/617357/random-pick-with-weight/
import itertools, bisect, random
class Solution:

    def __init__(self, w: List[int]):
        self.w = list(itertools.accumulate(w))  # Generate a list of indices where the distances between each pair are given weights

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))  # Randomly select a number from the range of indices and return the interval it falls into using binary search


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
