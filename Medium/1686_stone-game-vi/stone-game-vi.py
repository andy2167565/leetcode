class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        # Reference: https://leetcode.com/problems/stone-game-vi/solutions/969574/java-c-python-sort-by-value-sum/
        import operator
        values = sorted(zip(aliceValues, bobValues), key=sum, reverse=True)
        A = B = 0
        for i, (a, b) in enumerate(values):
            if i % 2:
                B += b
            else:
                A += a
        return operator.gt(A, B) - operator.lt(A, B)
