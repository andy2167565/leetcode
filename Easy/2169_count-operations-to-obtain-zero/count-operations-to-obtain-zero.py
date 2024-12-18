class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        return 0 if not num1 * num2 else num1 // num2 + self.countOperations(num2, num1 % num2)
