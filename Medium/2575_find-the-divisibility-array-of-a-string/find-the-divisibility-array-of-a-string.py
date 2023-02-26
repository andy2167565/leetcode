class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans, num = [], 0
        for digit in word:
            num = (num * 10 + int(digit)) % m
            ans.append(int(not num))
        return ans
