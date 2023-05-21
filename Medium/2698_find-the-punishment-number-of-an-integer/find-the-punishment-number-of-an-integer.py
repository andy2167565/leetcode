class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check(i, curr_sum, s):
            if i == len(s):
                return curr_sum == num
            result = False
            for j in range(i, len(s)):
                result = check(j + 1, curr_sum + int(s[i: j + 1]), s) or result
            return result

        ans = 0
        for num in range(1, n + 1):
            square = num * num
            if check(0, 0, str(square)):
                ans += square
        return ans
