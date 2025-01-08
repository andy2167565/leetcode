class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        for i, c in enumerate(bin(n)[:1:-1]):
            ans[i % 2] += int(c)
        return ans
