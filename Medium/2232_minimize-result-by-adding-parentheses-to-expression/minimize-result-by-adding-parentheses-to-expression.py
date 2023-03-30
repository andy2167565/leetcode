class Solution:
    def minimizeResult(self, expression: str) -> str:
        first, second = expression.split('+')
        score, ans = float('inf'), ''
        for i in range(len(first)):
            num1, num2 = int(first[:i] or 1), int(first[i:])
            for j in range(1, len(second) + 1):
                num3, num4 = int(second[:j]), int(second[j:] or 1)
                curr_score = num1 * (num2 + num3) * num4
                if curr_score < score:
                    score = curr_score
                    ans = f'{first[:i]}({first[i:]}+{second[:j]}){second[j:]}'
        return ans
