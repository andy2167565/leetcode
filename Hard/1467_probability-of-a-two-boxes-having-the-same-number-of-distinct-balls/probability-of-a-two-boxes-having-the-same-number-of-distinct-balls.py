class Solution:
    def getProbability(self, balls: List[int]) -> float:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/discuss/661723/Struggling-with-probability-problems-Read-this.
        import math
        self.ans = 0
        left, right = [0] * len(balls), [0] * len(balls)
        permutation = lambda n, x: math.factorial(n) / math.prod(math.factorial(i) for i in x)
        def dfs(i, sum1, sum2, color1, color2):
            if abs(sum1 - sum2) > sum(balls) - sum1 - sum2: return
            if i == len(balls):
                if color1 == color2:
                    self.ans += permutation(sum1, left) * permutation(sum2, right)
            else:
                for j in range(balls[i] + 1):
                    left[i], right[i] = j, balls[i] - j
                    dfs(i + 1, sum1 + j, sum2 + balls[i] - j, color1 + (j > 0), color2 + (balls[i] != j))
        dfs(0, 0, 0, 0, 0)
        return self.ans / permutation(sum(balls), balls)

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/discuss/661757/Python-10-Lines-90-Multionomial-coefficients-explained
        import math, itertools
        ans = 0
        cases = list(itertools.product(*(range(i + 1) for i in balls)))
        multinomial = lambda box: math.factorial(sum(box)) / math.prod(math.factorial(i) for i in box)
        for i in range(len(cases)):
            if sum(cases[i]) == sum(balls) // 2 and cases[i].count(0) == cases[~i].count(0):
                ans += multinomial(cases[i]) * multinomial(cases[~i])
        return ans / multinomial(balls)
