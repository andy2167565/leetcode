class Solution:
    def sumGame(self, num: str) -> bool:
        # Reference: https://leetcode.com/problems/sum-game/solutions/1330360/python-3-simple-math-explanation/
        question1 = question2 = sum1 = sum2 = 0
        for i in range(len(num) // 2):  # Get digit sum and question mark count for the first and second half of num respectively
            if num[i] == '?':
                question1 += 1
            else:
                sum1 += int(num[i])
            if num[~i] == '?':
                question2 += 1
            else:
                sum2 += int(num[~i])
        q, r = divmod(question2 - question1, 2)
        return not (not r and q * 9 == (sum1 - sum2))  # When Bob can't win, Alice wins
