class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return not num or bool(num % 10)
